#!/usr/bin/python
import pickle
import re
import sys


def collect_labelled_users(data=None, labels="../supportdata/output_files/titles_and_incomes.pickle",
                           output_dir="../supportdata/output_files/", debug=True):
    """

    :param data:
    :param labels:
    :param output_dir:
    :param debug:
    :return:
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

    # For every tweet in the input, find its author and try to label it

    # Determining if data is being put in via stdin or argument
    if data is not None:
        source = data
    else:
        source = sys.stdin

    for line in source:
        parts = line.split('\t')

        userid = int(parts[0])
        username = parts[1]
        screenname = parts[2]
        description = parts[3][:-1]

        # Make sure this user isn't already included in the collection
        if userid not in users_processed:
            result = pattern.search(description)

            try:
                occupation = result.group(0).lower()

                o_class = title_class_income[occupation][0]
                income = title_class_income[occupation][1]
                users_class_income[userid] = (username, screenname, description, occupation, o_class, income)

                users_processed.append(userid)

                if debug and result is not None:
                    print(userid, '\t', occupation)

            except AttributeError as A:
                # No label as result, moving on
                pass

            except KeyError as K:
                if debug:
                    print(K)

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
