#!/usr/bin/python
#   Type token ratio - Léon Melein, s2580861
#   Implements the type token ratio per user as a feature


def generate(tweets, debug=False):
    """
    Generates the type-token ratio for a user (S_TTR).

    :param tweets: a List containing a list of tokens per tweet.
    :param debug: a Bool indicating if debugging information should be printed (default: False).
    :return: a Dict containing the feature name as key and calculated ratio as value.
    """

    individual_types = []
    types, tokens = 0, 0

    # For every tweet, get the amount of tokens and types
    for tweet in tweets:

        # Count all tokens in the tweet
        tokens += len(tweet)

        # Collect all individual types included in the tweet
        for word in tweet:
            if debug:
                print(word, individual_types)

            if word not in individual_types:
                individual_types.append(word)

    # Count all types for a user
    types = len(individual_types)

    if debug:
        print(individual_types)
        print(types, tokens)

    # Calculate overall type-tokenratio
    ttr = types / tokens
    return {"S_TTR": ttr}


if __name__ == '__main__':
    print(generate([["hello", "world", "this",  "is", "is", "is", "is"],["i", "hope", "this", "works"]]))
