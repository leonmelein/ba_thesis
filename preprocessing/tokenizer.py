#!/usr/bin/python
import pickle

from preprocessing.tokenizers import sentencetokenizer, twittertokenizer
from preprocessing.punctuation import stripper


def tokenize(userfile="../supportdata/output_files/postselected_users.pickle", output_dir="../supportdata/output_files/",
             corpus="../corpus/", amount=500, debug=False):
    """
    Generates word tokens and sentence tokenized text for a given set of users. The word tokens are stored in a List
    containing a List per tweet, which holds that tweet's tokens. The sentence tokenized text holds tokens separated by
     spaces. Each new sentence is separated by a newline character.

    :param userfile: path to a Pickle file containing a dictionary with the class labels as keys and lists of user id's
    as values (String, default: ../supportdata/output_files/postselected_users.pickle).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param corpus: path to the tweet collection (String, default: ../corpus/).
    :param amount: amount of tweets to be used per user (Int, default: 500)
    :param debug: toggle to print debugging information (Bool, default: False).
    :return:
    """

    output_file = "tokenized_users.pickle"
    output = output_dir + output_file
    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    low, high = [], []

    # For every class, process its users
    for key, values in users.items():
        if debug:
            print(key, ":", values)

        # For each user, get the first 500 tweets and generate the tokens per tweet and sentence tokenized text
        i = 0
        for value in values:
            i += 1
            if debug:
                print(i)

            filepath = "{}{}/{}.txt".format(corpus, key, value)
            with open(filepath, "r") as inputfile:
                tweets = inputfile.readlines()[:amount]
                assert (len(tweets) == amount)

            # Create a list of tokens for every tweet,
            tokenized_tweets = twittertokenizer.tokenize(tweets)

            # Remove punctuation and lower each token
            tokenized_and_stripped_tweets = [stripper.strip(tweet, lower=True) for tweet in tokenized_tweets]

            # Create a list of sentences for every tweet
            # N.B. We use the non-lowered, non-stripped tweets as some readability measures depend on capitalization and
            # punctuation
            sent_tokenizer = sentencetokenizer.load_tokenizer()
            tokenized_sentences = []
            for tweet in tokenized_tweets:
                tokenized_sentences += sentencetokenizer.tokenize(" ".join(tweet), sent_tokenizer)
            tokenized_sentences_string = "\n".join(tokenized_sentences)

            # Save the tokenized data
            if key == "low":
                low.append((tokenized_and_stripped_tweets, tokenized_sentences_string))
            else:
                high.append((tokenized_and_stripped_tweets, tokenized_sentences_string))

            if debug:
                print(tokenized_tweets, "\n", tokenized_sentences)

    # Write the tokenized data to text
    with open(output, 'wb+') as outputfile:
        pickle.dump({"low": low, "high": high}, outputfile)

if __name__ == '__main__':
    tokenize(debug=False)
