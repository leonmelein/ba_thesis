import os
import pickle
from numpy.random import seed, choice


def post_select_users(corpus="../corpus/", output_dir="../supportdata/output_files/",
                      income_classes=("low", "high"), amount=1000, debug=False):

    output_file = "postselected_users.pickle"
    output = output_dir + output_file
    selected_per_class = {}

    for income_class in income_classes:
        if debug:
            print(income_class)

        # Get users available in class
        os.chdir(corpus+income_class)
        available_users = [(name[:-4]) for name in os.listdir(".")]

        # Select the chosen amount of users from class
        seed(42)
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
