#!/usr/bin/python
#   Word n-grams - Léon Melein, s2580861
from collections import defaultdict
import nltk


def generate(tweets, ngram="1-2-3", debug=False, binary=False):
    """
    Generates ngrams and ngram frequencies for a given user's tweets

    Partly based on an example by B. Plank  <https://github.com/bplank/BA-scriptie/blob/master/Combining_features.ipynb>

    :param tweets:  a List containing a list of tokens per tweet.
    :param ngram: a String indicating which ngrams to generate, each number divided by a - (default: "1-2-3")
    :param debug: a Bool indicating if debugging information should be printed (default: False).
    :param binary: a Bool indicating if the ngram count should be binary (default: False).
    :return:
    """

    PREFIX_WORD_NGRAM = "W:"

    # Dictionary that holds features for current instance, using a defaultdict in case we do not use a binary count
    if binary:
        d = {}
    else:
        d = defaultdict(int)

    # For every tweet, generate the requested n-grams and prefix them so they can be easily seen in our most
    # informative features
    for tweet in tweets:

        for n in ngram.split("-"):
            for gram in nltk.ngrams(tweet, int(n)):
                if debug:
                    print(gram)
                gram = str(n)+PREFIX_WORD_NGRAM + "_".join(gram)
                if binary:
                    d[gram] = 1
                else:
                    d[gram] += 1

    return d

if __name__ == '__main__':
    ngrams = generate([
        ["this", "is", "a", "tweet"],
        ["give", "me", "a", "good", "reason"],
        ["is", "your", "room", "locked"]
    ])
    for key, value in ngrams.items():
        print(key, value)
