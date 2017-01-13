#!/usr/bin/python
import pickle
import re
import sys


def collect_labelled_users(data=None, labels="../supportdata/output_files/titles_and_incomes.pickle",
                           output_dir="../supportdata/output_files/", debug=False):
    """
    Gathers users from the twitter2 corpus and labels them with their self disclosed occupational title from their
    description. The resulting dictionary, containing user id's as keys and Tuples containing username, real name,
     description, found occupation, occupational class and income as values, is written to disk with Pickle.

    :param data: input data created by tweet2tab, either loaded in via standard input or from file (default: stdin,
    optional: String containing path to file with exported data from tweet2tab)
    :param labels: path to Pickle file containing a Dictionary with occupational titles as keys and tuples with their
    occupational class and income as values (String, default: ../supportdata/output_files/titles_and_incomes.pickle).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param debug: toggle to print debugging information (Bool, default: False).
    :return: None
    """

    output_file = "labeled_users.pickle"
    output = output_dir + output_file
    users_class_income = {}
    users_processed = []

    with open(labels, 'rb') as f:
        title_class_income = pickle.load(f)

    # Generate search string from occupation titles
    regex = ""
    for title in title_class_income.keys():
        regex += "\\b" + re.escape(title) + "\\b|"
    regex = regex[:-1]
    pattern = re.compile(regex, re.IGNORECASE)

    # Determining if data is being put in via stdin or argument
    if data is not None:
        source = data
    else:
        source = sys.stdin

    # For every tweet in the input, find its author and try to label it with an occupation
    for line in source:
        parts = line.split('\t')

        userid = int(parts[0])
        username = parts[1]
        screenname = parts[2]

        # Make sure to strip off the newline of the description part, as it is the last part of the line
        description = parts[3][:-1]

        # Make sure this user isn't already included in the collection
        if userid not in users_processed:
            result = pattern.search(description)

            try:
                # Get the first found occupation with regex
                occupation = result.group(0).lower()

                # Get occupational class for found occupations
                o_class = title_class_income[occupation][0]
                income = title_class_income[occupation][1]

                # Save user info with label and occupational class in the output dict
                users_class_income[userid] = (username, screenname, description, occupation, o_class, income)

                # Add user to list of already processed users, so we do not process users twice, saving time
                users_processed.append(userid)

                if debug and result is not None:
                    print(userid, '\t', occupation)

            except AttributeError as A:
                # No label as result, moving on
                if debug:
                    print(A)

            except KeyError as K:
                # Could not find an income and/or occupational class.
                # Given that the labels dictionary is correctly structured, this shouldn't happen normally.
                if debug:
                    print(K)

    # Write labeled users to disk
    with open(output, 'wb+') as dumpfile:
        pickle.dump(users_class_income, dumpfile)

    if debug:
        print("Found users:", len(users_processed))


if __name__ == '__main__':
    if len(sys.argv) == 0:
        collect_labelled_users(debug=True)
    else:
        with open(sys.argv[1], "r") as inputfile:
            collect_labelled_users(data=inputfile.readlines(), debug=True)
