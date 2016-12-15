import string


def generate(tweets, debug=False):
    types, tokens = 0, 0
    for tweet in tweets:
        # Removal of punctuation
        punctuation = list(string.punctuation)
        punctuation.append("...")
        punctuation.append("…")

        # TODO: provide pretokenized tweets
        cleaned_text = []
        for item in tweet.split(" "):
            if item not in punctuation:
                cleaned_text.append(item)

        if debug:
            print(cleaned_text)

        # Tokens
        tokens += len(cleaned_text)

        # Types
        individual_types = []
        for item in cleaned_text:

            if debug:
                print(item, individual_types)

            if item not in individual_types:
                individual_types.append(item)

        types += len(individual_types)

    if debug:
        print(types, tokens)

    return {"TTR": types / tokens}


if __name__ == '__main__':
    print(generate(["hello world , this is is is is . i hope this works ... !"]))
