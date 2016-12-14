from collections import defaultdict
import nltk
import string

PREFIX_WORD_NGRAM = "W:"
PREFIX_CHAR_NGRAM = "C:"

# TODO: CHECK IF TWEET SEPARATOR WAS CHOSEN WRIGHT AND FILTERED OUT CORRECTLY

def generate(self, text, ngram="1-2-3", debug=False):
    """
    extracts word n-grams

    >>> f=Featurizer()
    >>> d = f._word_ngrams("this is a test",ngram="1-3")
    >>> len(d)
    6
    """

    # dictionary that holds features for current instance
    if self.binary:
        d = {}
    else:
        d = defaultdict(int)

    if self.lowercase:
        text = text.lower()
    words = text.split(self.DELIM)

    # Removal of punctuation
    punctuation = list(string.punctuation)
    punctuation.append("...")
    punctuation.append("…")

    if debug:
        print(punctuation)

    #if self.remove_stopwords:
    if debug:
        print(words)

    words = [w for w in words if w not in punctuation and w != " "]

    for n in ngram.split("-"):
        for gram in nltk.ngrams(words, int(n)):
            gram = PREFIX_WORD_NGRAM + "_".join(gram)
            if self.binary:
                d[gram] = 1  # binary
            else:
                d[gram] += 1

    return d
