#!/usr/bin/python
import pickle
import json
from datagathering.twitterapi import users_lookup, authentication


def check_users(userfile="../supportdata/output_files/labeled_users.pickle",
                output_dir="../supportdata/output_files/", debug=False):
    """

    :param userfile:
    :param output_dir:
    :param debug:
    :return:
    """

    output_file = "suitable_users.pickle"
    output = output_dir + output_file

    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    suitable_users = {}
    available_tokens = authentication.authenticate()
    flattened_values = [str(x) for x in list(users.keys())]

    # API limitation: we can only send 100 id's per request. Instead of splitting our list up manually,
    # we let the program handle it automatically
    # TODO: change to while loop
    chunks = chunk_list(flattened_values, 100)
    for chunk in chunks:
        userids = ",".join(chunk)
        if debug:
            print(userids)

        # Perform lookup of user profiles for a list of user id's
        info, available_tokens = users_lookup.request(userids, available_tokens, debug)
        user_info = json.loads(info)

        for user in user_info:
            # Get the status count and public status from the user profile
            userid, count, private = user['id'], user['statuses_count'], user['protected']

            # If a user has enough tweets and is set to public, save it
            if count > 1000 and private is False:
                suitable_users[userid] = users[userid]

    print("Users:", len(suitable_users.keys()))
    with open(output, "wb+") as outputfile:
        pickle.dump(suitable_users, outputfile)


# TODO: change this before sub
def chunk_list(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

if __name__ == '__main__':
    check_users(debug=True)
