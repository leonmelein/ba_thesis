#!/usr/bin/python
import pickle


def load_tokenizer(training="../supportdata/input_files/sentence_tokenizer_dutch.pickle"):
    """
    Loads a pretrained PunktSentenceTokenizer object from a Pickle file.

    :param training: String containing the path to the Pickle file.
    :return: a PunktSentenceTokenizer object.
    """
    with open(training, 'rb') as f:
        tokenizer = pickle.load(f)

    return tokenizer


def tokenize(tweet, tokenizer=load_tokenizer()):
    """
    Tokenizes tweet into the sentences it comprises.

    :param tweet: A list of tweets for a certain user.
    :param tokenizer: a pretrained PunktSentenceTokenizer object (default: load a tokenizer from file)
    :return: a list containing all sentences included in the tweet
    """
    return tokenizer.tokenize(tweet)

if __name__ == '__main__':
    sentences = tokenize("ik denk van wel . iets meer info zou helpen . als u contact opneemt met school hebben we een oriënterend gesprek")
