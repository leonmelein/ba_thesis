from nltk.tokenize import TweetTokenizer


def tokenize(tweets):
    """
    Tokenizes tweets using the TwitterTokenizer from the NLTK library: http://www.nltk.org/api/nltk.tokenize.html.
    Also removes user handles, URLs and hashtags using simple heuristics.
    :param tweets: A list of tweets for a certain user.
    :return: A list containing all tokenized tweets.
    """

    # You cannot name a file "tokenize.py" because that interferes with NLTK, are you kidding me...
    tokenizer = TweetTokenizer(strip_handles=True)
    tokenized_tweets = []

    for tweet in tweets:
        cleaned_tokens = []
        tokens = tokenizer.tokenize(tweet)
        for token in tokens:
            if token[:4] == "http":
                pass
            elif token[:1] == "#" and len(token) > 1:
                pass
            else:
                cleaned_tokens.append(token)
        tokenized_tweets.append(cleaned_tokens)

    return tokenized_tweets

if __name__ == '__main__':
    with open('../data_gathering/corpus/high/23235082.txt') as inputfile:
        print(tokenize(inputfile.readlines()))
