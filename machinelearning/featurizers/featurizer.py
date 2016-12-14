#!/usr/bin/python
from sklearn.base import TransformerMixin
from machinelearning.featurizers.surface import typetokenratio, fiveletterwordsratio, wordlength, tweetlength
from machinelearning.featurizers.ngrams import word_ngrams


class Featurizer(TransformerMixin):
    """Our own featurizer: extract features from each document for DictVectorizer"""

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        """
        here we could add more features!
        """
        out = []
        for text in X:
            # TODO: evaluate if we want to use ngrams
            ngrams = word_ngrams.generate(self, text, ngram=self.word_ngrams)
            # surface
            ttr = typetokenratio.generate(self, text)
            fivecharwordratio = fiveletterwordsratio.generate(self, text)
            wordlen = wordlength.generate(self, text)
            tweetlen = tweetlength.generate(self, text)

            # Prepare output dict
            out_dict = {}
            out_dict.update(ngrams)
            out_dict.update(ttr)
            out_dict.update(fivecharwordratio)
            out_dict.update(wordlen)
            out_dict.update(tweetlen)
            out.append(out_dict)
        return out

    def __init__(self, word_ngrams="1", binary=True, lowercase=False, remove_stopwords=False):
        """
        binary: whether to use 1/0 values or counts
        lowercase: convert text to lowercase
        remove_stopwords: True/False
        """
        self.DELIM = " "
        self.data = []  # will hold data (list of dictionaries, one for every instance)
        self.lowercase = lowercase
        self.binary = binary
        self.remove_stopwords = remove_stopwords
        self.stopwords = [] # No Dutch list of stopwords available...
        self.word_ngrams = word_ngrams

if __name__ == "__main__":
    import doctest
    doctest.testmod()
