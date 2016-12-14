import string


def generate(self, text, debug=False):
    # Removal of punctuation
    punctuation = list(string.punctuation)
    punctuation.append("...")
    punctuation.append("…")

    cleaned_text = []
    for item in text.split(" "):
        if item not in punctuation:
            cleaned_text.append(item)

    if debug:
        print(cleaned_text)

    no_of_words = len(cleaned_text)
    totallength = 0
    for word in cleaned_text:
        totallength += len(word)

    if debug:
        print(totallength, no_of_words)

    return {"WL": totallength / no_of_words}

if __name__ == '__main__':
    print(generate(None,
                   "I sure hope this works ! I don't know what to do otherwise ...",
                   debug=True))
