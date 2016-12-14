# TODO: FIX PUNCTUATION MESS
import string


def generate(instance, text, debug=False):
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

    # of words
    total_no_words = len(cleaned_text)

    # of words longer than 5 chars
    longer_than_5_chars = 0
    for item in cleaned_text:

        if debug:
            print(item, longer_than_5_chars)

        if len(item) > 5:
            longer_than_5_chars += 1

    if debug:
        print("Total # of words:", total_no_words, "- # longer than 5 chars:", longer_than_5_chars)

    return {"5CHWR": longer_than_5_chars / total_no_words}

if __name__ == '__main__':
    print(generate(None, "I sure hope this works ! I don't know what to do otherwise ..."))
