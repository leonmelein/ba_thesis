

def generate(tweets, debug=False):
    length_in_words = 0
    length_in_chars = 0

    for tweet in tweets:
        for word in tweet:
            length_in_words += 1
            length_in_chars += len(word)

    if debug:
        print("S_TLW:", length_in_words, "S_TLCH:", length_in_chars)

    return {"S_TLW": length_in_words, "S_TLCH": length_in_chars, "RWL": length_in_chars / length_in_words}


if __name__ == '__main__':
    print(generate([["dit", "is",  "een", "schande"]]))

