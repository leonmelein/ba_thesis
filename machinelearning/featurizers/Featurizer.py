#!/usr/bin/python
# Featurizer
# Léon Melein, s2580861

from sklearn.base import TransformerMixin
from machinelearning.featurizers.surface import typetokenratio, fiveletterwordsratio, tweetlengths
from machinelearning.featurizers.ngrams import word_ngrams
from machinelearning.featurizers.readability import measures


class Featurizer(TransformerMixin):
    """
    A featurizer that implements (most of) the surface and readability features used by Flekova et al. (2016), as well
    as n-gram features.

    Partly based on an example by B. Plank <https://github.com/bplank/BA-scriptie/blob/master/Combining_features.ipynb>
    """

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        """
        Transforms user texts into usable features for use with an sklearn classifier.

        :param X: tuple containing a user's tweets as lists of tokens and a String containing all tokenized sentences
        of a user, divided by newline characters (\n).
        :return: a Dict containing all calculated metrics as key-value pairs.
        """

        out = []
        for text in X:
            tweets = text[0]
            sentences = text[1]

            out_dict = {}
            # N-grams
            if "ngrams" in self.feature_set:
                ngrams = word_ngrams.generate(tweets, ngram=self.word_ngrams, binary=self.binary)
                out_dict.update(ngrams)

            # Surface
            if "surface" in self.feature_set:
                type_token_ratio = typetokenratio.generate(tweets, self.debug)
                ratio_of_5ch_words = fiveletterwordsratio.generate(tweets, self.debug)
                tweet_length = tweetlengths.generate(tweets, self.debug)
                out_dict.update(type_token_ratio)
                out_dict.update(ratio_of_5ch_words)
                out_dict.update(tweet_length)

            # Readability
            if "readability" in self.feature_set:
                readability_metrics = measures.generate(sentences)
                out_dict.update(readability_metrics)

            # Add features for user to overall list
            out.append(out_dict)
        return out

    def __init__(self, word_ngrams="1-2-3", feature_set=("ngrams", "surface", "readability"), binary=False, debug=False):
        """
        Initializes a new Featurizer instance.

        word_ngrams: a String indicating which ngrams to generate, each number divided by a - (default: "1-2-3")
        binary: a Bool indicating if the ngram count should be binary (default: False).
        debug: a Bool indicating if debugging information should be printed (default: False).
        """
        self.debug = debug
        self.binary = binary
        self.word_ngrams = word_ngrams
        self.feature_set = feature_set

if __name__ == "__main__":
    import doctest
    doctest.testmod()
