import string


def generate(tweets, debug=False):
    types, tokens = 0, 0
    for tweet in tweets:
        # Tokens
        tokens += len(tweet)

        # Types
        individual_types = []
        for word in tweet:
            if debug:
                print(word, individual_types)

            if word not in individual_types:
                individual_types.append(word)

        types += len(individual_types)

    if debug:
        print(types, tokens)

    return {"S_TTR": types / tokens}


if __name__ == '__main__':
    print(generate(["hello world , this is is is is . i hope this works ... !"]))
