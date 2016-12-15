from collections import defaultdict
import nltk
import string

PREFIX_WORD_NGRAM = "W:"
PREFIX_CHAR_NGRAM = "C:"

# TODO: CHECK IF TWEET SEPARATOR WAS CHOSEN WRIGHT AND FILTERED OUT CORRECTLY

def generate(tweets, ngram="1-2-3", debug=False, binary=True, delim=" ", lowercase=False):
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
        if lowercase:
            tweet = tweet.lower()
        words = tweet.split(delim)

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
                print(gram)
                gram = PREFIX_WORD_NGRAM + "_".join(gram)
                if binary:
                    d[gram] = 1  # binary
                else:
                    d[gram] += 1

    return d

if __name__ == '__main__':
    ngrams = generate(["this is a tweet . ", "give me a good reason ! ", "is your room locked ? "])
    for key, value in ngrams.items():
        print(key, value)
