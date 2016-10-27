import csv
import sys
import pickle


def import_incomes(filename, delimit=";"):
    class_income = {}
    average_hours_per_year = 1677

    # Load CSV file with example occupational titles
    with open(filename, newline='') as csvfile:
        incomes = csv.reader(csvfile, delimiter=delimit)
        for row in incomes:
            submajor_group = int(row[0])
            hourly_income = float(row[1])
            yearly_income = round(hourly_income * average_hours_per_year, 2)
            class_income[submajor_group] = yearly_income

        # Save occupational dict to disk
        with open('output_files/class_income.pickle', 'wb+') as f:
            pickle.dump(class_income, f)

        print(class_income)

if len(sys.argv) == 0:
    "You must pass a comma separated file for importing!"
else:
    import_incomes(sys.argv[1])
