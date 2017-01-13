#!/usr/bin/python
import langid
import json
import pickle
import os
from datagathering.twitterapi import authentication, user_timeline


def gather_user_posts(userfile="../supportdata/output_files/preselected_users.pickle",
                      output_dir="../corpus/", debug=False):
    """
    Gathers self written Dutch posts for each user in a class. Disregards users with less than 500 suitable posts.
    The posts are written to a text file with the user id as name in the folder of the the user's income class.

    :param userfile: path to a Pickle file containing a Python dictionary with the class labels as keys and Lists with
    the selected user id's as values (String, default: ../supportdata/output_files/preselected_users.pickle).
    :param output_dir: path to output directory (String, default: ../supportdata/output_files).
    :param debug: toggle to print debugging information (Bool, default: False).
    :return: None
    """

    available_auths = authentication.authenticate()
    with open(userfile, "rb") as inputfile:
        users = pickle.load(inputfile)

    # For each class, collect user posts
    for key in users.keys():
        # Print ID per user
        if debug:
            print(key)

        # Create directory for class, if necessary
        directory = os.path.expanduser(output_dir + key)
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)

        # Create a list of already downloaded users, to make sure we don't do work twice
        already_collected = [int(name[:-4]) for name in os.listdir(".")]

        for userid in users[key]:

            # If the user hasn't been downloaded,
            # collect their tweets and check if the user is suitable for our research
            if userid not in already_collected:
                applicable_tweets = []

                # Get the latest 1600 tweets per user (8 pages x 200 tweets)
                for i in range(1, 8):
                    content, available_auths = user_timeline.request(userid, available_auths, i, debug)

                    # If a page exists, load its contents
                    if content is not None:
                        tweets = json.loads(content)

                        # For every tweet on the page, check if it is self written and Dutch
                        for tweet in tweets:
                            post = tweet['text']
                            if post[:2] != "RT" and post != "":
                                # If post is written in Dutch, add to list of usable tweets
                                if langid.classify(post)[0] == "nl":
                                        applicable_tweets.append(post)

                # Show total amount of usable tweets for a user
                if debug:
                    print(userid, "# of suitable tweets:", len(applicable_tweets))

                # If a user has enough suitable tweets, write the user's tweets to disk
                if len(applicable_tweets) >= 500:
                    with open("{}.txt".format(userid), 'a+') as file_handler:
                        for post in applicable_tweets:
                                file_handler.write(post.replace("\n", " ") + "\n")


if __name__ == '__main__':
    gather_user_posts(debug=True)

