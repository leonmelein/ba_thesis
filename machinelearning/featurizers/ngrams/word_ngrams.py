from collections import defaultdict
import nltk

PREFIX_WORD_NGRAM = "W:"


def generate(tweets, ngram="1-2-3", debug=False, binary=False,):
    """
    extracts word n-grams
    Based on the example provided by Ms Plank
    <https://github.com/bplank/BA-scriptie/blob/master/Combining_features.ipynb>
    """

    # dictionary that holds features for current instance
    if binary:
        d = {}
    else:
        d = defaultdict(int)

    for tweet in tweets:

        for n in ngram.split("-"):
            for gram in nltk.ngrams(tweet, int(n)):
                if debug:
                    print(gram)
                gram = PREFIX_WORD_NGRAM + "_".join(gram)
                if binary:
                    d[gram] = 1  # binary
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
