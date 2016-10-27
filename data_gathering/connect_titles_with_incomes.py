import csv
import sys
import pickle


def importOccupationalTitles(filename, delimit=";"):
    title_class_income = {}

    with open('output_files/class_income.pickle', 'rb') as f:
        class_income = pickle.load(f)

    # Load CSV file with example occupational titles
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimit)
        for row in spamreader:
            submayor_group = int(row[0][:2])

            try:
                # Try to get income for class
                income = class_income[submayor_group]
                raw_occupational_titles = [x.strip() for x in row[2].split(',')]

                print(submayor_group, "-", raw_occupational_titles, "-", income)
                for title in raw_occupational_titles:
                        title_class_income[title.lower()] = (submayor_group, income)

            except KeyError:
                # If class not found, don't add it to the dict and continue with next
                # TODO: add proper error handling
                pass

        # Save occupational dict to disk
        with open('output_files/title_class_income.pickle', 'wb+') as f:
            pickle.dump(title_class_income, f)

        print(title_class_income)

if len(sys.argv) == 0:
    "You must pass a comma separated file for importing!"
else:
    importOccupationalTitles(sys.argv[1])
