# Example given by Barbara in class
# TODO: learn from, use and remove in final submission
from sklearn.base import TransformerMixin


class TextStats(TransformerMixin):
    """Extract features from each document for DictVectorizer"""

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        " extract length of each data instance "
        out= [{'length': len(text)}
                for text in X]
        return out