#!/usr/bin/python
import csv
import sys
import pickle


def connect_titles_with_incomes(titles, incomes="../supportdata/output_files/incomes_per_submajor_group.pickle",
                                delimit=";", output_dir="../supportdata/output_files/", debug=False):
    """
    Imports example occupation titles for each submajor groups, links them to the average yearly income for their
    submajor group. The resulting dictionary, containing occupational titles as keys and Tuples with submajor group and
    yearly income as values, is written to disk with Pickle.

    :param titles: path to CSV file with example occupations titles (String).
    :param incomes: path to a Pickle file containing a dictionary with submajor groups as keys and
    average yearly incomes as values (String, default: ../supportdata/output_files/incomes_per_submajor_group.pickle).
    :param delimit: the field delimiter used in the CSV file (String, default: ;).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param debug: toggle to print debugging information (Bool, default: False).
    :return: None
    """

    output_file = "titles_and_incomes.pickle"
    output = output_dir + output_file
    title_class_income = {}

    with open(incomes, 'rb') as f:
        class_income = pickle.load(f)

    # Load CSV file with example occupational titles
    with open(titles, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimit)
        for row in spamreader:
            submayor_group = int(row[0][:2])

            try:
                # Try to get income for class
                income = class_income[submayor_group]
                raw_occupational_titles = [x.strip() for x in row[2].split(',')]

                if debug:
                    print(submayor_group, "-", raw_occupational_titles, "-", income)

                # For each occupational title, save its submajor group and average yearly income
                for title in raw_occupational_titles:
                        title_class_income[title.lower()] = (submayor_group, income)

            except KeyError as K:
                # If class not found, don't add it to the dict and continue with next. This should not happen,
                # but it is considered good practice to use error handling with a dictionary lookup.
                if debug:
                    print(K)

    # Show contents of resulting dictionary
    if debug:
        for key, value in title_class_income.items():
            print(key, "-", value)

    # Save resulting dictionary to disk
    with open(output, 'wb+') as f:
        pickle.dump(title_class_income, f)


if __name__ == '__main__':
    if len(sys.argv) == 0:
        "You must pass a comma separated file for importing!"
    else:
        connect_titles_with_incomes(sys.argv[1])
