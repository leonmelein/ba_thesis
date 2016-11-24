#!/usr/bin/python
import TwitterSearch
import pickle
import os
import json
import random
from TwitterSearch import TwitterSearchException, TwitterUserOrder, TwitterSearch


def connect_twitter():
    path = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/private/credentials.json")
    cred = json.load(open(path))
    twitter = TwitterSearch(
        access_token=cred["ACCESS_TOKEN"],
        access_token_secret=cred["ACCESS_TOKEN_SECRET"],
        consumer_key=cred["CONSUMER_KEY"],
        consumer_secret=cred["CONSUMER_SECRET"]
    )
    return twitter


def main(user_dict):
    """
    Removes users that:
    (1) Have an insufficient number of tweets
    (2) Have deleted or otherwise modified their profile, so that it can no longer be found by the Twitter API

    :param user_dict:
    :return:
    """
    low = []
    high = []
    not_enough_tweets, not_found, no_tweets = 0, 0, 0
    ts = connect_twitter()

    #for key in user_dict.keys():
    key = "high"
    values = user_dict["high"]
    random.shuffle(values)

    for item in values:
        twitter_user_order = TwitterUserOrder(int(item[0]))
        try:
            tweets = ts.search_tweets_iterable(twitter_user_order)

            # Get number of tweets, disregard users with less than 500 tweets
            no_of_tweets = tweets['content'][000]['user']['statuses_count']
            if no_of_tweets >= 500:
                if key == "low":
                    low.append(item)
                else:
                    high.append(item)
            else:
                print(item[0], "has not enough tweets, skipping")
                not_enough_tweets += 1

        except TwitterSearchException as e:
            #print(item[0], " could not be found, skipping")
            print(item[0], e)
            not_found += 1

        except KeyError:
            print(item[0], "has no tweets, skipping")
            no_tweets += 1

    # Export selected users to new dictionary
    export_dict = {'high': high}

    # Save selected, divided users
    with open('output_files/cleaned_divided_users_high.pickle', 'wb+') as outputfile:
        pickle.dump(export_dict, outputfile)

    # Print outcomes
    print("\nRemaining # of users in high and low class")
    #print("Low:", len(export_dict['low']))
    print("High:", len(export_dict['high']))
    #print("\nReasons for removal")
    #print("Not enough tweets:", not_enough_tweets)
    #print("User not found:", not_found)
    #print("User has no tweets:", no_tweets)

    print("\nCleaned selection has been saved to disk.")

with open('output_files/divided_user_class_income.pickle', 'rb') as inputfile:
    userdict = pickle.load(inputfile)
    main(userdict)
