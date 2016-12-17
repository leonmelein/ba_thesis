

def generate(tweets, debug=False):

    longer_than_5_chars = 0
    total_no_words = 0
    for tweet in tweets:

        # of words
        total_no_words += len(tweet)

        # of words longer than 5 chars
        for word in tweet:

            if debug:
                print(word, longer_than_5_chars)

            if len(word) > 5:
                longer_than_5_chars += 1

    if debug:
        print("Total # of words:", total_no_words, "- # longer than 5 chars:", longer_than_5_chars)

    return {"S_5CH": longer_than_5_chars / total_no_words}

if __name__ == '__main__':
    print(
        generate(
            [
                ["I", "sure", "hope", "this", "works", "I", "don't", "know", "what", "to", "do", "otherwise"]
            ]
        )
    )
