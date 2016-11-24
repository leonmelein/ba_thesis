import pickle
import re
import sys


def classifyUsers():
    users_class_income = {}
    users_processed = []

    with open('output_files/title_class_income.pickle', 'rb') as f:
        title_class_income = pickle.load(f)

    # Generate search string from occupation titles
    regex = ""
    for title in title_class_income.keys():
        regex += "\\b"+re.escape(title)+"\\b|"
    regex = regex[:-1]
    pattern = re.compile(regex, re.IGNORECASE)

    found_occupations = 0
    # Try to find an occupation for each user
    #with open(userfile, 'r') as users:
    #    for line in users:
    for line in sys.stdin:
            parts = line.split('\t')

            userid = parts[0]
            username = parts[1]
            screenname = parts[2]
            description = parts[3][:-1]

            if userid not in users_processed:
                result = pattern.search(description)

                try:
                    occupation = result.group(0).lower()
                    print(userid, '\t', occupation)

                    o_class = title_class_income[occupation][0]
                    income = title_class_income[occupation][1]
                    users_class_income[userid] = (username, screenname, description, o_class, income)

                    #current_class_content = users_with_occupational_class.get(occupational_class, [])
                    #new_class_content = current_class_content
                    #new_class_content.append((userid, username, screenname, description, occupation))
                    #users_with_occupational_class[occupational_class] = new_class_content

                    users_processed.append(userid)
                    found_occupations += 1
                except AttributeError:
                    pass

                except KeyError:
                    print("You did it wrong...")

    with open('output_files/user_class_income.pickle', 'wb+') as dumpfile:
        pickle.dump(users_class_income, dumpfile)

    print("Found occupations:", found_occupations)
    print("Found users:", len(users_processed))

if __name__ == '__main__':
    classifyUsers()
