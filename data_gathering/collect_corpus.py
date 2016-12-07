import pickle
import json
import os
import time
import langid

from TwitterSearch import TwitterSearchException
from TwitterSearch import TwitterUserOrder, TwitterSearch


def collect(users):
    ts = connectTwitter()
    for key in users.keys():
        for user in users[key]:
            getTweets(int(user), key, ts)


def connectTwitter():
    path = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/private/credentials.json")
    cred = json.load(open(path))
    twitter = TwitterSearch(access_token=cred["ACCESS_TOKEN"],access_token_secret=cred["ACCESS_TOKEN_SECRET"],
                            consumer_key=cred["CONSUMER_KEY"], consumer_secret=cred["CONSUMER_SECRET"])
    return twitter


def getTweets(userid, final_income_class, ts):
    directory = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/corpus/" + final_income_class)
    filename = "{}.txt".format(userid)
    twitter_user_order = TwitterUserOrder(userid)

    try:
        # Get all tweets without RT's (max 3200)
        all_tweets = []

        for tweet in ts.search_tweets_iterable(twitter_user_order, callback=handle_rate_limits):
            tweet = tweet['text']
            # Filter out retweets
            if tweet[:2] != "RT":
                # Check if tweet is in Dutch
                # TODO: remove url's from tweets
                if langid.classify(tweet)[0] == "nl":
                    if tweet != "":
                        all_tweets.append(tweet)

        # If user has enough tweets, save tweets to file
        if len(all_tweets) > 500:
            print("Saved ", userid, "at", time.strftime("%H:%M", time.localtime(time.time())))
            if not os.path.exists(directory):
                os.makedirs(directory)
            os.chdir(directory)

            with open(filename, 'w+') as file_handler:
                for tweet in all_tweets:
                    tweet = tweet.replace("\n", "")
                    file_handler.write("{}\n".format(tweet))

    except TwitterSearchException as twe:
        print(twe.args)


def handle_rate_limits(current_ts_instance):  # accepts ONE argument: an instance of TwitterSearch
    queries, tweets_seen = current_ts_instance.get_statistics()
    if queries > 0 and (queries % 128) == 0:  # trigger delay every 128th query
        print("Rate limit triggered", queries)
        time.sleep(30)  # sleep for 30 seconds

with open("output_files/autoselected_users.pickle", "rb") as file:
    users = pickle.load(file)
    collect(users)
