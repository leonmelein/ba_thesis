#!/usr/bin/python
import pickle


def create_income_classes(userfile="../supportdata/output_files/suitable_users.pickle",
                          output_dir="../supportdata/output_files/"):
    """
    Divides users into high and low income classes, based on their labeled income.
    This uses the average income in the Netherlands to seperate between both classes.
    The resulting cleaned dictionary, containing the class labels as keys and Lists containing a List per user with its
    user id as Int and user information in a Tuple, is written to disk with Pickle.

    :param userfile: path to a Pickle file containing a dictionary with user id's as keys and
    Tuples with user information as values (String, default: ../supportdata/output_files/suitable_users.pickle).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :return: None
    """

    divided = {}
    output_file = "users_in_classes.pickle"
    output = output_dir + output_file

    # Load user info
    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    # Classify each user
    for userid in users.keys():
        # Get income for user
        income = users[userid][5]

        # Categorize user in the right income class for a two-way split (Flekova et al.) using the average income
        # for the Netherlands
        if income > 34500:
            currentvalue = divided.get("high", [])
            currentvalue.append([userid, users[userid]])
            divided["high"] = currentvalue
        elif income < 34500:
            currentvalue = divided.get("low", [])
            currentvalue.append([userid, users[userid]])
            divided["low"] = currentvalue

    # Print classification statistics
    print("low:", len(divided["low"]),
          "high:", len(divided["high"]))

    # Save classified user to disk
    with open(output, 'wb+') as outputfile:
        pickle.dump(divided, outputfile)


if __name__ == '__main__':
    create_income_classes(debug=True)
