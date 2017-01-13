import os
import pickle
from numpy.random import seed, choice


def post_select_users(corpus="../corpus/", output_dir="../supportdata/output_files/",
                      income_classes=("low", "high"), amount=1000, debug=False):
    """
    Selects a given amount of users per class from a file-based corpus, stores those users per class in a Dictionary and
    writes that dictionary to disk using Pickle.

    :param corpus: path to the tweet collection (String, default: ../corpus/).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param income_classes: the classes for which users have to be selected and folders exist in the corpus
    (Tuple, default: ("low", "high"))
    :param amount: the amount of users to be selected per class (Int, default: 100).
    :param debug: toggle to print debugging information (Bool, default: False).
    :return: None
    """

    output_file = "postselected_users.pickle"
    output = output_dir + output_file
    selected_per_class = {}

    # For each income class, select a given amount of users
    for income_class in income_classes:
        if debug:
            print(income_class)

        # Get users available in class
        os.chdir(corpus+income_class)
        available_users = [(name[:-4]) for name in os.listdir(".")]

        # Using 42 as seed to ensure reproducible results
        # "Answer to the Ultimate Question of Life, The Universe, and Everything"
        # - The Hitchhiker's Guide to the Galaxy
        seed(42)

        # Select the chosen amount of users from class
        selected_users = choice(available_users, amount, replace=False).tolist()
        assert(len(selected_users) == amount)
        selected_per_class[income_class] = selected_users

        # Move back to top dir for next class
        os.chdir("..")

    if debug:
        print(selected_per_class)

    with open(output, 'wb+') as outputfile:
        pickle.dump(selected_per_class, outputfile)

if __name__ == '__main__':
    post_select_users(debug=True)
