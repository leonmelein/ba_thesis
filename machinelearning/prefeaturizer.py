#!/usr/bin/python
from machinelearning.featurizers.Featurizer import Featurizer
import pickle


def main(userfile="../supportdata/output_files/tokenized_users.pickle", ngrams="1-2-3", feature_set=("ngrams", "surface", "readability"),
         output_dir="../supportdata/output_files/", filename="", debug=False):
    """
    Loads user data from dictionary with pretokenized user information and generates features. The resulting
    dictionary with the classes as keys and a List, holding a dictonary of features per user, as values, is written
    to disk with Pickle.

    Partly based on an example by B. Plank <https://github.com/bplank/BA-scriptie/blob/master/Combining_features.ipynb>

    :param userfile: A pickled dictionary containing:
        -   Two income classes as keys: "low" and "high"
        -   Tokenized tweets and sentence tokenized tweets for user in that class as value.
    :return: None.
    """
    output_file = "prefeaturized_users_"+filename+".pickle"
    output = output_dir + output_file
    prefeatured_users = {}

    # Load income classes from dict
    with open(userfile, "rb") as inputfile:
        userdata = pickle.load(inputfile)

    # For every class, transform the user data to a dictionary containing every feature and save that dictionary
    for key, values in userdata.items():
        if debug:
            print(key)
        featurizer = Featurizer(word_ngrams=ngrams, feature_set=feature_set, binary=True)
        prefeaturized_data = featurizer.transform(values)
        prefeatured_users[key] = prefeaturized_data

    # Write dictionary with features to disk
    if debug:
        print("Saving...")
    with open(output, "wb+") as outputfile:
        pickle.dump(prefeatured_users, outputfile)

if __name__ == '__main__':
    main(debug=True)
