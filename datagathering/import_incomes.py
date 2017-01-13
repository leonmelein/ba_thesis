#!/usr/bin/python
import csv
import sys
import pickle


def import_incomes(file, output_dir="../supportdata/output_files/", average_hours_per_year=1677, delimit=";",
                   debug=False):
    """
    Imports average hourly incomes for submajor groups from a CSV file and converts them to average yearly incomes.
    The resulting dictionary, containing user id's as keys and tuples containing username, real name,
     description, found occupation, occupational class and incomes, is written to disk with Pickle.

    :param file: path to CSV file (String).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param average_hours_per_year: average hours worked by a Dutch user per year (Int, default: 1677).
    :param delimit: the field delimiter used in the CSV file (String, default: ;).
    :param debug: toggle to print debugging information (Bool, default: False).
    :return:
    """

    output_file = "incomes_per_submajor_group.pickle"
    output = output_dir + output_file
    class_income = {}

    # Load CSV file with example occupational titles
    with open(file, newline='') as csvfile:
        incomes = csv.reader(csvfile, delimiter=delimit)

        # For each submajor group, calculate its yearly income and save to disk
        for row in incomes:
            submajor_group = int(row[0])
            hourly_income = float(row[1])
            yearly_income = round(hourly_income * average_hours_per_year, 2)
            class_income[submajor_group] = yearly_income

        # Save dict with submajor groups and their incomes to disk
        with open(output, 'wb+') as f:
            pickle.dump(class_income, f)

        if debug:
            print(class_income)

if __name__ == '__main__':
    if len(sys.argv) == 0:
        "You must pass a comma separated file for importing!"
    else:
        import_incomes(sys.argv[1])
