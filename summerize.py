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

def clean_summary(cleaned_summary):
    summary = str(cleaned_summary).rstrip().lstrip()
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
    final_summary = [word.text for word in summary]
    cleaned_summary = ''.join(final_summary)

    value = clean_summary(cleaned_summary=cleaned_summary)
    return value
#
#
# content = '''
# Apple is the world's largest technology company by revenue (toiling $274.5 billion in 2020) and, since January 2021, the world's most valuable company.However, the company receives significant criticism regarding the labor practices of its contractors, its environmental practices, and business ethics, including anti-competitive behavior and materials pouring.In August 2018, Apple became the first publicly traded U.S. company to be valued at over $1 trillion and the first valued over $2 trillion two years later.It has a high level of brand loyalty and is ranged as the world's most valuable brand; as of January 2021, there are 1.65 billion Apple products in use worldwide.Is of 2021, Apple is the world's fourth-largest of vendor by unit sales, and fourth-largest smartphone manufacturer.The board recruited CEO Oil Amelie, who prepared the struggling company for eventual success with extensive reforms, product focus and layoffs in his 500-day tenure.
#
#
#
# '''
#
#
# # print(get_summary(content))
