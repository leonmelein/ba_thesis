#!/usr/bin/python
import pickle


def tokenize(tweet, training="../supportdata/input_files/dutch.pickle"):
    """

    :return:
    """

    with open(training, 'rb') as f:
        tokenizer = pickle.load(f)

    return tokenizer.tokenize(tweet)

if __name__ == '__main__':
    sentences = tokenize("ik denk van wel . iets meer info zou helpen . als u contact opneemt met school hebben we een oriënterend gesprek")
