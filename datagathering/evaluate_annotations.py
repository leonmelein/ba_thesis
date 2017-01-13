#!/usr/bin/python
from collections import defaultdict
import pickle
import random


def evaluate_annotations(userfile="../supportdata/output_files/users_in_classes.pickle", amount_per_class=100,
                         debug=False):
    """

    :param userfile:
    :param amount_per_class:
    :param debug:
    :return:
    """

    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    low = []
    high = []
    not_a_person, hobby_volunteer, study, wrong_occupation, miscellaneous = 0, 0, 0, 0, 0
    wronged_occupation = defaultdict(int)

    for key in users.keys():
        values = users[key]
        random.seed(42)
        random.shuffle(values)

        if debug:
            print(key)
        i = 0
        while i < amount_per_class:
            item = values[i]

            # Print selection statistics
            print("\n=== Low: {} | High: {} | Progress: {} / {} ===".format(len(low), len(high), i, amount_per_class))

            # Print user info
            formatstring = "\nID:\t{}\nReal name:\t{}\nUsername:\t{}\nDescription:\t{}\nOccupation:\t{}\n"
            twid, username, real_name, description, occupation = item[0], item[1][0], item[1][1], item[1][2], item[1][3]
            print(formatstring.format(
                twid,
                real_name,
                username,
                description,
                occupation
            ))

            # Get annotator judgment
            answer = "a"
            while answer not in ["", "1", "2", "3", "4", "5"]:
                print("""Is this a real, correctly labeled user?\n
[Yes: ENTER; 1 - Not a person; 2 - Hobby/Volunteer; 3 - Study; 4 - Wrong occupation; 5 - Miscellaneous]""", end="\n")
                answer = input()

            # Process user in accordance with judgment
            if answer == "":
                if key == "low":
                    low.append(item)
                else:
                    high.append(item)
            else:
                reason = int(answer)

                if reason == 1:
                    not_a_person += 1
                elif reason == 2:
                    hobby_volunteer += 1
                elif reason == 3:
                    study += 1
                elif reason == 4:
                    wrong_occupation += 1
                    wronged_occupation[occupation] += 1
                else:
                    miscellaneous += 1
            i += 1

    # Print outcomes
    print("\nRemaining # of users in high and low class")
    print("Low:", len(low))
    print("High:", len(high))

    print("\n\nReasons to exclude users (w/# of users)")
    print("User")
    print("- User not a person:", not_a_person)
    print("Occupation")
    print("- Occupation is hobby/voluntary:", hobby_volunteer)
    print("- Occupation is study:", study)
    print("- Occupation is plain wrong:", wrong_occupation)
    print("-- Wrong occupations:", sorted(wronged_occupation.items()))
    print()
    print("Miscellaneous:", miscellaneous)

if __name__ == '__main__':
    evaluate_annotations()
