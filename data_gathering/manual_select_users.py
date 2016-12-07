#!/usr/bin/python
from collections import defaultdict
import pickle
import random

low = []
high = []


def main(user_dict):
    not_a_person, hobby_volunteer, study, wrong_occupation, miscellaneous = 0, 0, 0, 0, 0
    tested_users = []
    wronged_occupation = defaultdict(int)

    for key in user_dict.keys():
        values = user_dict[key]
        random.shuffle(values)

        print(key)
        i = 0
        while i < 100:
            item = values[i]
            tested_users.append(item)

            # Print selection statistics
            print("\n=== Low:", len(low), "High:", len(high), "===")

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
                print("Is this a real, correctly labeled user?\n[Yes: ENTER; No: 1 - Not a person; 2 - Hobby/Volunteer; 3 - Study; 4 - Wrong occupation; 5 - Miscellaneous]", end="\n")
                answer = input()

            # Process user in accordance with judgment
            if answer == "":
                if key == "low":
                    low.append(item)
                else:
                    high.append(item)
            else:
                reason = int(answer)
                while reason not in [1, 2, 3, 4, 5]:
                    print("Why is it not?")
                    reason = int(input())

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

    # Export selected users to new dictionary
    export_dict = {'low': low, 'high': high}

    # Save selected, divided users
    with open('output_files/selected_divided_users_TEST.pickle', 'wb+') as outputfile:
        pickle.dump(export_dict, outputfile)

    # Print outcomes
    print("\nRemaining # of users in high and low class")
    print("Low:", len(export_dict['low']))
    print("High:", len(export_dict['high']))

    print("\n\nReasons to exclude users (w/# of users)")
    print("User")
    print("- User not a person:", not_a_person)
    print("Occupation")
    print("- Occupation is hobby/voluntary:", hobby_volunteer)
    print("- Occupation is study:", study)
    print("- Occupation is plain wrong:", wrong_occupation)
    print("Wrong occupations:", sorted(wronged_occupation.items()))
    print()
    print("Miscellaneous:", miscellaneous)

    print("\nSelection has been saved to disk.")

with open('output_files/divided_user_class_income_SELECT.pickle', 'rb') as inputfile:
    userdict = pickle.load(inputfile)
    main(userdict)
