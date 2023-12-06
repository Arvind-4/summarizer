import re
import spacy
from heapq import nlargest
from string import punctuation
from functools import lru_cache
from spacy.lang.en.stop_words import STOP_WORDS


def remove_bracketed_words(text):
    cleaned = re.sub(r"\[([^\[\]]*?)\]", "", text)
    return cleaned


def get_word_frequencies(doc):
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    return word_frequencies


def get_sentence_scores(sentence_tokens, word_frequencies):
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    return sentence_scores


@lru_cache()
def summarize(text: str, per: float = 0.3):
    nlp = spacy.load("en_core_web_sm")
    text = remove_bracketed_words(text)
    doc = nlp(text)
    word_frequencies = get_word_frequencies(doc)

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = get_sentence_scores(sentence_tokens, word_frequencies)

    select_length = int(len(sentence_tokens) * per)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = "".join(final_summary)
    summary = remove_bracketed_words(summary)
    return summary
