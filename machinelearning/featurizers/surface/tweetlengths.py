#!/usr/bin/python
#   Tweet lengths - Léon Melein, s2580861


def generate(tweets, debug=False):
    """
    Generates the following length measures per user:

    -   Total tweet length in words         (S_TLW)
    -   Total tweet length in characters    (S_TLCH)
    -   Relative word length per user       (S_RWL)

    :param tweets: a list containing a list of tokens per tweet (List).
    :param debug: toggle indicating if debugging information should be printed (Bool, default: False).
    :return: a Dictionary containing the feature names as keys and calculated lengths as values.
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
