#!/usr/bin/python
import pickle
import json
from datagathering.twitterapi import users_lookup, authentication


def check_users(userfile="../supportdata/output_files/labeled_users.pickle",
                output_dir="../supportdata/output_files/", debug=False):
    """
    Checks if a given collection of user id's if the corresponding user still exists, has more than 1000 tweets and has
    a public profile. This ensures the user can be used for further research. The resulting cleaned dictionary,
    containing user id's as keys and Tuples containing username, real name, description, found occupation, occupational
    class and income as values, is written to disk with Pickle.

    :param userfile: path to a Pickle file containing a dictionary with user id's as keys and
    Tuples with user information as values (String, default: ../supportdata/output_files/labeled_users.pickle).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param debug: toggle to print debugging information (Bool, default: False).
    :return: None
    """

    output_file = "suitable_users.pickle"
    output = output_dir + output_file

    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    suitable_users = {}
    available_tokens = authentication.authenticate()

    # Create a list of user id's from user dictionary
    flattened_values = [str(x) for x in list(users.keys())]

    # API limitation: we can only send 100 id's per request. Instead of splitting our list up manually,
    # we let the program handle it automatically
    chunks = chunk_list(flattened_values, 100)
    for chunk in chunks:
        userids = ",".join(chunk)
        if debug:
            print(userids)

        # Perform lookup of user profiles for a list of user id's
        info, available_tokens = users_lookup.request(userids, available_tokens, debug)
        user_info = json.loads(info)

        # For every user the API returns (this excluded deleted profiles)
        for user in user_info:
            # Get the status count and public status from the user profile
            userid, count, private = user['id'], user['statuses_count'], user['protected']

            # If a user has enough tweets and is set to public, save it
            if count > 1000 and private is False:
                suitable_users[userid] = users[userid]

    print("Users:", len(suitable_users.keys()))
    with open(output, "wb+") as outputfile:
        pickle.dump(suitable_users, outputfile)


def chunk_list(list, chunk_size):
    chunk_size = max(1, chunk_size)
    return (list[i:i + chunk_size] for i in range(0, len(list), chunk_size))

if __name__ == '__main__':
    check_users(debug=True)
