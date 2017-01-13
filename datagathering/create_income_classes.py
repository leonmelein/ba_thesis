#!/usr/bin/python
import pickle


def create_income_classes(userfile="../supportdata/output_files/suitable_users.pickle",
                          output_dir="../supportdata/output_files/", debug=False):
    """

    :param userfile:
    :param output_dir:
    :param debug:
    :return:
    """

    divided = {}
    output_file = "users_in_classes.pickle"
    output = output_dir + output_file

    # Load users
    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    for userid in users.keys():
        # Get income for user
        income = users[userid][5]

        # Categorize user in the right income class for a two-way split (Flekova et al.)
        if income > 34500:
            currentvalue = divided.get("high", [])
            currentvalue.append([userid, users[userid]])
            divided["high"] = currentvalue
        elif income < 34500:
            currentvalue = divided.get("low", [])
            currentvalue.append([userid, users[userid]])
            divided["low"] = currentvalue


    # Show keys in resulting classes
    if debug:
        print(divided.keys())

    # Print class statistics
    print("low:", len(divided["low"]),
          "high:", len(divided["high"]))

    with open(output, 'wb+') as outputfile:
        pickle.dump(divided, outputfile)


if __name__ == '__main__':
    create_income_classes(debug=True)
