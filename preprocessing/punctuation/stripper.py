#!/usr/bin/python
import string


def strip(tokens, lower=False):
    """
    Strips known punctuation characters from tokens.

    :param tokens: the individual tokens per tweet (List).
    :param lower: toggle indicating if all tokens should be lowercased (Bool, default: False).
    :return:
    """

    # Removal of punctuation
    punctuation = list(string.punctuation)
    punctuation.append("...")
    punctuation.append("…")

    if lower:
        clean_tokens = [token.lower() for token in tokens if token not in punctuation]
    else:
        clean_tokens = [token for token in tokens if token not in punctuation]

    return clean_tokens

if __name__ == '__main__':
    print(strip("......//////./?!!!#"))

