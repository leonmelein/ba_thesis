import string


def generate(tweets, debug=False):

    # Removal of punctuation
    punctuation = list(string.punctuation)
    punctuation.append("...")
    punctuation.append("…")
    punctuation.append("")  # TODO: remove from final version

    length_in_words = 0
    length_in_chars = 0

    for tweet in tweets:
        words_no_punct = []
        for word in tweet.split(" "):
            if word not in punctuation:
                length_in_words += 1
                words_no_punct.append(word.rstrip())
                length_in_chars += len(word)

        if debug:
            print(words_no_punct)

    if debug:
        print("TLW:", length_in_words, "TLCH:", length_in_chars)

    return {"TLW": length_in_words, "TLCH": length_in_chars}


if __name__ == '__main__':
    print(generate(["dit is een schande !", "vanavond om 20:00 de premiere van de almanak . ", "auw, mijn hand ! "]))

