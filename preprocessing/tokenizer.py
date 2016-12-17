#!/usr/bin/python
import pickle

from preprocessing.tokenizers import sentencetokenizer, twittertokenizer
from preprocessing.punctuation import stripper


def main(userfile="../supportdata/output_files/postselected_users.pickle", output_dir="../supportdata/output_files/",
         corpus="../corpus/", amount=500, debug=False):

    output_file = "tokenized_users.pickle"
    output = output_dir + output_file

    low, high = [], []

    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    for key, values in users.items():
        if not debug:
            print(key, ":", values)

        i = 0
        for value in values:
            i += 1
            print(i)

            filepath = "{}{}/{}.txt".format(corpus, key, value)
            with open(filepath, "r") as inputfile:
                tweets = inputfile.readlines()[:amount]
                assert (len(tweets) == amount)

            #   Create a list with a string of tokens for every tweet, each token separated with a space
            tokenized_tweets = twittertokenizer.tokenize(tweets)
            tokenized_and_stripped_tweets = [stripper.strip(tweet) for tweet in tokenized_tweets]

            #   Create a list of sentences for every tweet
            sent_tokenizer = sentencetokenizer.load_tokenizer()
            tokenized_sentences = []
            for tweet in tokenized_tweets:
                tokenized_sentences += sentencetokenizer.tokenize(" ".join(tweet), sent_tokenizer)
            tokenized_sentences_string = "\n".join(tokenized_sentences)

            if key == "low":
                low.append((tokenized_and_stripped_tweets, tokenized_sentences_string))
            else:
                high.append((tokenized_and_stripped_tweets, tokenized_sentences_string))

            if debug:
                print(tokenized_tweets, "\n", tokenized_sentences)

            with open(output, 'wb+') as outputfile:
                pickle.dump({"low": low, "high": high}, outputfile)

if __name__ == '__main__':
    main(debug=False)
