#!/usr/bin/python
import TwitterSearch
import pickle
import os
import json
import random
import time
import numpy
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

    for key in user_dict.keys():
        values = user_dict[key]
        random.shuffle(values)

        for item in values:
            twitter_user_order = TwitterUserOrder(int(item[0]))
            twitter_user_order.set_include_rts(True)
            try:
                i = 0
                for tweet in ts.search_tweets_iterable(twitter_user_order, callback=handle_rate_limits):
                    i += 1

                if i >= 500:
                    print(item[0], i)
                    if key == "low":
                        low.append(item)
                    else:
                        high.append(item)

            except TwitterSearchException as e:
                print(item[0], e)
                not_found += 1

            except KeyError:
                print(item[0], "has no tweets, skipping")
                no_tweets += 1

    # Export selected users to new dictionary
    export_dict = {'high': high, 'low':low}

    # Save selected, divided users
    with open('output_files/cleaned_divided_users_high.pickle', 'wb+') as outputfile:
        pickle.dump(export_dict, outputfile)

    # Print outcomes
    print("\nRemaining # of users in high and low class")
    print("Low:", len(export_dict['low']))
    print("High:", len(export_dict['high']))
    #print("\nReasons for removal")
    #print("Not enough tweets:", not_enough_tweets)
    #print("User not found:", not_found)
    #print("User has no tweets:", no_tweets)

    print("\nCleaned selection has been saved to disk.")

def handle_rate_limits(current_ts_instance):  # accepts ONE argument: an instance of TwitterSearch
    queries, tweets_seen = current_ts_instance.get_statistics()
    if queries > 0 and (queries % 64) == 0:  # trigger delay every 128th query
        print("Rate limit triggered", queries)
        time.sleep(30)  # sleep for 30 seconds

with open('output_files/divided_user_class_income_SELECT.pickle', 'rb') as inputfile:
    userdict = pickle.load(inputfile)
    main(userdict)
