#!/usr/bin/python
import string


def strip(tokens, lower=False):
    """

    :param tokens:
    :param lower:
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

