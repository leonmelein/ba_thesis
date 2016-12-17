#!/usr/bin/python
import pickle


def main():
    with open("../supportdata/output_files/tokenized_users.pickle", "rb") as inputfile:
        userdata = pickle.load(inputfile)

    user_count = 0
    for key, values in userdata.items():

        new_values = []
        for value in values:
            tweets = value[0]
            sentences = value[1]
            sentence_string = "\n".join(sentences)
            new_values.append((tweets, sentence_string))

            user_count += 1
            print(user_count)

        userdata[key] = new_values

    with open("../supportdata/output_files/sentenced_tokenized_users.pickle", "wb+") as outputfile:
        pickle.dump(userdata, outputfile)

if __name__ == '__main__':
    main()
