# TODO: FIX PUNCTUATION MESS
import string


def generate(tweets, debug=False):
    # Removal of punctuation
    punctuation = list(string.punctuation)
    punctuation.append("...")
    punctuation.append("…")

    longer_than_5_chars = 0
    total_no_words = 0
    for tweet in tweets:

        cleaned_tweet = []
        for item in tweet.split(" "):
            if item not in punctuation:
                cleaned_tweet.append(item)

        if debug:
            print(cleaned_tweet)

        # of words
        total_no_words += len(cleaned_tweet)

        # of words longer than 5 chars
        for item in cleaned_tweet:

            if debug:
                print(item, longer_than_5_chars)

            if len(item) > 5:
                longer_than_5_chars += 1

    if debug:
        print("Total # of words:", total_no_words, "- # longer than 5 chars:", longer_than_5_chars)

    return {"5CHWR": longer_than_5_chars / total_no_words}

if __name__ == '__main__':
    print(generate(["I sure hope this works ! I don't know what to do otherwise ..."]))
