import pickle
import json
import langid
import os

from TwitterSearch import TwitterSearchException
from TwitterSearch import TwitterUserOrder, TwitterSearch


def divide(users, type="twoway"):
    divided = {}

    for userid in users.keys():
        # Flekova et al. Two Way split: low - high
        if type == "twoway":
            income = users[userid][4]
            if income > 34500:
                currentvalue = divided.get("high", [])
                currentvalue.append(userid)
                divided["high"] = currentvalue
            else:
                currentvalue = divided.get("low", [])
                currentvalue.append(userid)
                divided["low"] = currentvalue


        # CBS Five Way split: 0-10 10-20 20-30 30-40 40-50 50-
        elif type == "fiveway":
            income = users[userid][4]
            if income < 10000:
                currentvalue = divided.get("0", [])
                currentvalue.append(userid)
                divided["0"] = currentvalue
            elif 10000 < income < 20000:
                currentvalue = divided.get("10", [])
                currentvalue.append(userid)
                divided["10"] = currentvalue
            elif 20000 < income < 30000:
                currentvalue = divided.get("20", [])
                currentvalue.append(userid)
                divided["20"] = currentvalue
            elif 30000 < income < 40000:
                currentvalue = divided.get("30", [])
                currentvalue.append(userid)
                divided["30"] = currentvalue
            elif 40000 < income < 50000:
                currentvalue = divided.get("40", [])
                currentvalue.append(userid)
                divided["40"] = currentvalue
            else:
                currentvalue = divided.get("50", [])
                currentvalue.append(userid)
                divided["50"] = currentvalue

    if type == "twoway":
        print("low:", len(divided["low"]),
              "high:", len(divided["high"]))
    elif type == "fiveway":
        print("0-10:", len(divided["0"]),
              "10-20:", len(divided["10"]),
              "20-30:", len(divided["20"]),
              "30-40:", len(divided["30"]),
              "40-50:", len(divided["40"]),
              "50-:", len(divided["50"]))

    return divided


def collect(users):
    for key in users.keys():
        for user in users[key]:
            print(user, key)
            getTweets(int(user), key)


def connectTwitter():
    path = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/private/credentials.json")
    cred = json.load(open(path))
    twitter = TwitterSearch(access_token=cred["ACCESS_TOKEN"],access_token_secret=cred["ACCESS_TOKEN_SECRET"],
                            consumer_key=cred["CONSUMER_KEY"], consumer_secret=cred["CONSUMER_SECRET"])
    return twitter


def getTweets(userid, final_income_class):
    ts = connectTwitter()
    directory = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/corpus/" + final_income_class)
    filename = "{}.txt".format(userid)
    twitter_user_order = TwitterUserOrder(userid)

    try:
        # Get all tweets without RT's (max 3200)
        all_tweets = []

        for tweet in ts.search_tweets_iterable(twitter_user_order):
            # Filter out retweets
            if tweet['text'][:2] != "RT":
                # Check if tweet is in Dutch
                # TODO: remove url's from tweets
                if langid.classify(tweet['text'])[0] == "nl":
                    all_tweets.append(tweet)

        # If user has enough tweets, save tweets to file
        if len(all_tweets) > 500:
            print("Length sufficient")
            if not os.path.exists(directory):
                os.makedirs(directory)
            os.chdir(directory)
            print(os.getcwd())

            with open(filename, 'w+') as file_handler:
                for tweet in all_tweets:
                    file_handler.write("{}\n".format(tweet['text']))
    except TwitterSearchException as twe:
        print(twe.args)


with open("output_files/user_class_income.pickle", "rb") as file:
    users = pickle.load(file)
    division = divide(users, "twoway")
    collect(division)
