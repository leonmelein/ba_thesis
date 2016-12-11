#!/usr/bin/python
import pickle


def create_income_classes(userfile="../supportdata/output_files/suitable_users.pickle",
                          output_dir="../supportdata/output_files/", type="twoway", debug=False):

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
        if type == "twoway":
            if income > 34500:
                currentvalue = divided.get("high", [])
                currentvalue.append([userid, users[userid]])
                divided["high"] = currentvalue
            else:
                currentvalue = divided.get("low", [])
                currentvalue.append([userid, users[userid]])
                divided["low"] = currentvalue

        # Categorize user in the right income class for a six-way split (Statistics Netherlands)
        elif type == "fiveway":
            if income < 10000:
                currentvalue = divided.get("0", [])
                currentvalue.append(userid)
                divided["0"] = currentvalue
            elif 10000 < income < 20000:
                currentvalue = divided.get("10", [])
                currentvalue.append(userid)
                divided["10"] = currentvalue
            elif 20000 < income < 30000:
                currentvalue = divided.get("20", [])
                currentvalue.append(userid)
                divided["20"] = currentvalue
            elif 30000 < income < 40000:
                currentvalue = divided.get("30", [])
                currentvalue.append(userid)
                divided["30"] = currentvalue
            elif 40000 < income < 50000:
                currentvalue = divided.get("40", [])
                currentvalue.append(userid)
                divided["40"] = currentvalue
            else:
                currentvalue = divided.get("50", [])
                currentvalue.append(userid)
                divided["50"] = currentvalue

    # Show keys in resulting classes
    if debug:
        print(divided.keys())

    # Print class statistics
    if type == "twoway":
        print("low:", len(divided["low"]),
              "high:", len(divided["high"]))
    elif type == "fiveway":
        print("0-10:", len(divided["0"]),
              "10-20:", len(divided["10"]),
              "20-30:", len(divided["20"]),
              "30-40:", len(divided["30"]),
              "40-50:", len(divided["40"]),
              "50-:", len(divided["50"]))

    with open(output, 'wb+') as outputfile:
        pickle.dump(divided, outputfile)


if __name__ == '__main__':
    create_income_classes(debug=True)

