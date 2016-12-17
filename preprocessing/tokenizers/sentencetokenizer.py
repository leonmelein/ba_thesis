#!/usr/bin/python
import pickle


def load_tokenizer(training="../supportdata/input_files/dutch.pickle"):
    with open(training, 'rb') as f:
        tokenizer = pickle.load(f)

    return tokenizer


def tokenize(tweet, tokenizer=load_tokenizer()):
    """

    :return:
    """
    return tokenizer.tokenize(tweet)

if __name__ == '__main__':
    sentences = tokenize("ik denk van wel . iets meer info zou helpen . als u contact opneemt met school hebben we een oriënterend gesprek")
