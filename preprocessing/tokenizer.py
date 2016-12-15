#!/usr/bin/python
from preprocessing import sentencetokenizer, twittertokenizer
import pickle


def main(userfile="../supportdata/output_files/postselected_users.pickle", output_dir="../supportdata/output_files/",
         corpus="../corpus/", amount=500, debug=False):

    output_file = "tokenized_users.pickle"
    output = output_dir + output_file

    low, high = [], []

    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    for key, values in users.items():
        if debug:
            print(key, ":", values)

        for value in values:
            if debug:
                print(value)

            filepath = "{}{}/{}.txt".format(corpus, key, value)
            with open(filepath, "r") as inputfile:
                tweets = inputfile.readlines()[:amount]
                assert (len(tweets) == amount)

            #   Create a list with a string of tokens for every tweet, each token separated with a space
            tokenized_tweets = twittertokenizer.tokenize(tweets)

            #   Create a list of sentences for every tweet
            tokenized_sentences = []
            for tweet in tokenized_tweets:
                tokenized_sentences += sentencetokenizer.tokenize(tweet)

            if key == "low":
                low.append((tokenized_tweets, tokenized_sentences))
            else:
                high.append((tokenized_tweets, tokenized_sentences))

            if debug:
                #print(tokenized_tweets, tokenized_sentences)
                pass

            with open(output, 'wb+') as outputfile:
                pickle.dump({"low": low, "high": high}, outputfile)

if __name__ == '__main__':
    main(debug=True)
