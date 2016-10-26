import pickle
import sys
import re
import sys


def classifyUsers(userfile):
    classified_users = {}
    users_handled = []

    with open('occupational_dict.pickle', 'rb') as f:
        title_class = pickle.load(f)
    # Generate search string

    with open(userfile, 'r') as users:
        for line in users:
            parts = line.split('\t')

            # TODO: modify to other format
            userid = parts[0]
            # username = parts[1]
            # screenname = parts[2]
            # description = parts[3][:-1]
            description = parts[1][:-1]

            if userid not in users_handled:
                occupational_titles = list(title_class.keys())

                # Hack to heighten the recursion limit
                sys.setrecursionlimit(10000)
                occupation = searchOccupation(description, occupational_titles)

                print(userid, ' | ', occupation)

                try:
                    if occupation is not None:
                        occupational_class = classified_users[occupation]
                        current_class = classified_users.get(occupational_class, [])
                        classified_users[occupational_class] = current_class.append((userid, description, occupation))
                        users_handled.append(userid)
                except KeyError:
                    # TODO: Add error handling?
                    pass

    with open('classified_users.pickle', 'wb+') as dumpfile:
        pickle.dump(classified_users, dumpfile)


def searchOccupation(description, terms):
    if len(terms) > 0:
        pattern = re.compile("\\b"+re.escape(terms[0])+"\\b", re.IGNORECASE)
        result = pattern.search(description)

        if result is not None:
            return result.group(0)
        else:
            if len(terms) > 1:
                return searchOccupation(description, terms[1:])
            else:
                return None
    else:
        return None

if len(sys.argv) == 0:
    "You must pass a tab separated file with users for processing!"
else:
    classifyUsers(sys.argv[1])
    #classifyUsers('biotest.txt')
    pass
