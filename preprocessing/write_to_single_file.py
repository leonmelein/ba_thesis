import pickle

from preprocessing.tokenizers import twittertokenizer


def write_to_single_file(userfile="../supportdata/output_files/postselected_users.pickle", corpus="../corpus/",
                         amount=500, debug=False):

    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    # For every class, merge all users in one text file
    for key, values in users.items():
        if debug:
            print(key, ":", values)

        # For each user
        for value in values:
            if debug:
                print(value)

            filepath = "{}{}/{}.txt".format(corpus, key, value)
            with open(filepath, "r") as inputfile:
                tweets = inputfile.readlines()[:amount]
                assert(len(tweets) == amount)

            # Tokenize tweets
            tokenized_tweets = twittertokenizer.tokenize(tweets)
            detokenized_tweets = []
            for tokenized_tweet in tokenized_tweets:
                # lower all words, just in case... TODO: re-evaluate
                detokenized_tweets.append(" ".join(tokenized_tweet).lower()+" ;")

            if debug:
                print(detokenized_tweets)

            userstring = " ".join(detokenized_tweets) + "\n"
            filepath = "../data/income.{}".format(key)
            with open(filepath, "a+") as outputfile:
                outputfile.write(userstring)

if __name__ == '__main__':
    write_to_single_file(debug=True)
