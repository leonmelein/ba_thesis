#!/usr/bin/python
#   Tweet lengths - Léon Melein, s2580861
#   Implements total tweet length in words and characters, as well was relative word length per user as features


def generate(tweets, debug=False):
    """
    Generates the total tweet length in both words and characters per user, as well as relative word length per user.

    :param tweets: a List containing a list of tokens per tweet.
    :param debug: a Bool indicating if debugging information should be printed (default: False).
    :return: a Dict containing the feature names as keys and calculated lengths as values.
    """
    length_in_words = 0
    length_in_chars = 0

    # For every tweet, count the words in it and the length of them
    for tweet in tweets:
        for word in tweet:
            length_in_words += 1
            length_in_chars += len(word)

    if debug:
        print("S_TLW:", length_in_words, "S_TLCH:", length_in_chars)

    return {"S_TLW": length_in_words, "S_TLCH": length_in_chars, "S_RWL": length_in_chars / length_in_words}


if __name__ == '__main__':
    print(generate([
        ["dit", "is",  "een", "schande"]
    ]))
