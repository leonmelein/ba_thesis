#!/usr/bin/python
import string


def strip(tokens):
    # Removal of punctuation
    punctuation = list(string.punctuation)
    punctuation.append("...")
    punctuation.append("…")

    clean_tokens = [token for token in tokens if token not in punctuation]
    return clean_tokens

if __name__ == '__main__':
    print(strip("......//////./?!!!#"))

