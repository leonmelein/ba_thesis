import pickle
import numpy


def pre_select_users(userfile="../supportdata/output_files/users_in_classes.pickle", amount=2000,
                     output_dir="../supportdata/output_files/", debug=False):
    """
    Preselection of users for retrieval of posts. From every class, 2000 users are randomly selected. The resulting
    dictionary with the classes as keys and a list of selected user id's as values, is written to disk with Pickle.

    Their latest tweets will be collected later on. Even though we use only 1000 users in our research,
    a sizable chunk of users will be discarded in the next step as they won't have enough self written Dutch tweets.

    :param userfile: path to a Pickle file containing a Python dictionary with the class labels as keys and
    Lists containing a List per user with its user id as Int and user information in a Tuple.
    (default: ../supportdata/output_files/users_in_classes.pickle)
    :param amount: the amount of users per class to be selected (Int, default: 2000).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param debug: toggle to print debugging information (Bool, default: False).
    :return: None
    """

    output_file = "preselected_users.pickle"
    output = output_dir + output_file
    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)
    autoselected_users = {}

    # Using 42 as seed to ensure reproducible results
    # "Answer to the Ultimate Question of Life, The Universe, and Everything"
    # - The Hitchhiker's Guide to the Galaxy
    numpy.random.seed(42)

    # For each class, select the chosen amount of users
    for key in users.keys():
        if debug:
            print(key)

        # Flatten userlist to User ID's only for use with NumPy
        flattened_values = [value[0] for value in users[key]]
        if debug:
            print(flattened_values)

        # Select chosen amount of users at random
        random_chosen = numpy.random.choice(flattened_values, amount, replace=False)
        autoselected_users[key] = random_chosen.tolist()

    # Write dictionary with selected users to disk
    with open(output, 'wb+') as outputfile:
        pickle.dump(autoselected_users, outputfile)

if __name__ == '__main__':
    pre_select_users(debug=True)
