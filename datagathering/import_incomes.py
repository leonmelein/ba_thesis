#!/usr/bin/python
import csv
import sys
import pickle


def import_incomes(filename, output_dir="../supportdata/output_files/", average_hours_per_year=1677, delimit=";"):
    output_file = "incomes_per_submajor_group.pickle"
    output = output_dir + output_file
    class_income = {}

    # Load CSV file with example occupational titles
    with open(filename, newline='') as csvfile:
        incomes = csv.reader(csvfile, delimiter=delimit)

        # For each submajor group, calculate its yearly income and save to disk
        for row in incomes:
            submajor_group = int(row[0])
            hourly_income = float(row[1])
            yearly_income = round(hourly_income * average_hours_per_year, 2)
            class_income[submajor_group] = yearly_income

        # Save occupational dict to disk
        with open(output, 'wb+') as f:
            pickle.dump(class_income, f)

        print(class_income)

if __name__ == '__main__':
    if len(sys.argv) == 0:
        "You must pass a comma separated file for importing!"
    else:
        import_incomes(sys.argv[1])
