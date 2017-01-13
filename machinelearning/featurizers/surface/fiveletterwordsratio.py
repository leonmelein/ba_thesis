#!/usr/bin/python
#   Five letter words ratio - Léon Melein, s2580861


def generate(tweets, debug=False):
    """
    Generates the ratio of words longer than 5 characters to the amount of all words per user (S_5CH).

    :param tweets: a List containing a list of tokens per tweet.
    :param debug: a Bool indicating if debugging information should be printed (default: False).
    :return: a Dict containing the feature name as key and calculated ratio as values.
    """

    longer_than_5_chars = 0
    total_no_words = 0

    # For every tweet, get the amount of words and the amount of those that are longer than 5 chars
    for tweet in tweets:

        # Count the total number of words
        total_no_words += len(tweet)

        # Count the total number of words longer than 5 chars
        for word in tweet:

            if debug:
                print(word, longer_than_5_chars)

            if len(word) > 5:
                longer_than_5_chars += 1

    if debug:
        print("Total # of words:", total_no_words, "- # longer than 5 chars:", longer_than_5_chars)

    # Calculate the >5 characters words ratio
    return {"S_5CH": longer_than_5_chars / total_no_words}

if __name__ == '__main__':
    print(generate([
                ["I", "sure", "hope", "this", "works", "I", "don't", "know", "what", "to", "do", "otherwise"]
        ]))
