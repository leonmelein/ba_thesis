import pickle
import numpy


def pre_select_users(userfile="../supportdata/output_files/users_in_classes.pickle", amount=2000,
                     output_dir="../supportdata/output_files/", debug=False):
    """

    :param userfile:
    :param amount:
    :param output_dir:
    :param debug:
    :return:
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

    with open(output, 'wb+') as outputfile:
        pickle.dump(autoselected_users, outputfile)

if __name__ == '__main__':
    pre_select_users(debug=True)
