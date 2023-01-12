import spacy
import re
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

stopwords = STOP_WORDS
punctuation = f'{punctuation}\n'
word_frequencies = sentence_scores = {}


def clean_data(content):
    clean_text = re.sub(r'\[\d+\]', '', content)
    return clean_text


def get_word_frequencies(doc):
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    return word_frequencies


def get_max_frequencies(word_frequencies):
    max_frequencies = max(word_frequencies.values())
    return max_frequencies


def get_sentence_scores(sentence_tokens):
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    return sentence_scores

def clean_summary(string):
    summary = str(string).rstrip().lstrip()
    return summary

def get_summary(content):
    nlp = spacy.load('en_core_web_sm')
    cleaned_content = clean_data(content=content)
    doc = nlp(cleaned_content)

    tokens = [token.text for token in doc]
    value = get_word_frequencies(doc=doc)
    value_max_frequency = get_max_frequencies(value)

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / value_max_frequency

    sentence_tokens = [sentence for sentence in doc.sents]
    value_sentence_score = get_sentence_scores(sentence_tokens)
    select_length = int(len(sentence_tokens) * 0.3)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    new_summary = ""
    for word in summary:
        new_summary += str(word)
    value = clean_summary(new_summary)
    return value
