#!/usr/bin/python
# Featurizer
# Léon Melein, s2580861

from sklearn.base import TransformerMixin
from machinelearning.featurizers.surface import typetokenratio, fiveletterwordsratio, tweetlengths
from machinelearning.featurizers.ngrams import word_ngrams
from machinelearning.featurizers.readability import measures


class Featurizer(TransformerMixin):
    """Our own featurizer: extract features from each document for DictVectorizer"""

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        """
        Extract features from user data.
        """

        out = []
        for text in X:
            tweets = text[0]
            sentences = text[1]

            # NGrams
            # TODO: evaluate if we want to use ngrams
            ngrams = word_ngrams.generate(tweets, ngram=self.word_ngrams, binary=self.binary)

            # Surface
            type_token_ratio = typetokenratio.generate(tweets, self.debug)
            ratio_of_5ch_words = fiveletterwordsratio.generate(tweets, self.debug)
            tweet_length = tweetlengths.generate(tweets, self.debug)

            # Readability
            readability_metrics = measures.generate(sentences)

            # Prepare output dict

            out_dict = {}
            out_dict.update(ngrams)
            out_dict.update(type_token_ratio)
            out_dict.update(ratio_of_5ch_words)
            out_dict.update(tweet_length)
            out_dict.update(readability_metrics)
            out.append(out_dict)
        return out

    def __init__(self, word_ngrams="1-2-3", binary=False, debug=False):
        """
        debug: print debugging information
        binary: whether to use 1/0 values or counts
        word_ngrams: which ngrams to generate, divided by a -
        """
        self.debug = debug
        self.binary = binary
        self.word_ngrams = word_ngrams

if __name__ == "__main__":
    import doctest
    doctest.testmod()
