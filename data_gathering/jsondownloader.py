import langid
import requests
import json
import pickle
import os
from requests_oauthlib import OAuth1


def main(userids):
    available_auths = getAuth()

    for key in userids.keys():
    # for key in ["low"]:
        print(key)
        directory = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/corpus/" + key)
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)

        already_collected = [int(name[:-4]) for name in os.listdir(".")]

        for user in userids[key]:
            userid = int(user)
            #print(userid)

            if userid not in already_collected:
                applicable_tweets = []
                for i in range(1, 18):
                    content, available_auths = request(userid, available_auths, i)
                    if content is not None:
                        tweets = json.loads(content)
                        for tweet in tweets:
                            post = tweet['text']
                            if post[:2] != "RT":
                                # Check if tweet is in Dutch
                                # TODO: remove url's from tweets
                                if langid.classify(post)[0] == "nl":
                                    if tweet != "":
                                        applicable_tweets.append(post)

                print(userid, "No:", len(applicable_tweets))
                if len(applicable_tweets) >= 500:
                    with open("{}.txt".format(userid), 'a+') as file_handler:
                        for post in applicable_tweets:
                                file_handler.write(post.replace("\n", " ") + "\n")


def request(userid, available_auths, page):
    user_request = request_user_timeline(userid, available_auths, page)

    if user_request.status_code == 200:
        try:
            print(user_request.headers['x-rate-limit-remaining'])
        except KeyError:
            pass
        return user_request.text, available_auths

    elif user_request.status_code == 429:
        available_auths.pop(0)

        if available_auths == []:
            available_auths = getAuth()

        return request(userid, available_auths, page)

    else:
        return None, available_auths


def request_user_timeline(userid, available_auths, page):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    payload = {'user_id': userid, 'count': 200, 'page':page}
    r = requests.get(url, auth=available_auths[0], params=payload)
    return r


def getAuth():

    # TODO: move to file!!!!
    auth1 = OAuth1("F16nWhKOrEsRz60OnWcGubbk2",
                   "ybx3BXgB0udVQh3G75CNN64K1Mw2DRGOuTnX7hRWwtCVd31WCb",
                   "27243865-tavl85onf1KIM5e7Lxm0lJ4WbwumPI3RYigrhzIPw",
                   "gAJvvo4tVHDS5R2v1db9AV4lp0ZrNgOYy3EMG7S7SQmzB")

    auth2 = OAuth1("YFKw0Pci64kC7l46zuHu2RXu4",
                   "h0mITAZ1bObBACvFpxFsHPbniguoAqy9waa2zoIJbjBK4NQxFa",
                   "27243865-1Diy3xDPHmkdJ2ki3bEbe4AGmMCyKqHqsE6YNPB0e",
                   "cm2fSk40oFhZEm00S4Juxa7lP0UKmyOJFf0TpPqrfWi1t")

    auth3 = OAuth1("DH0pgmtID2oD3QKZwnpn7kjCv",
                   "aCVhESAKIjlDHC5Pov4X2rwMmXBB7i4GsLWE45Kv6D50b8MDZ7",
                   "27243865-01SJ0xdnDIi57tmyPiyPaQ9pNfSQ2ULQPAIHqZRQf",
                   "t1D6KwhuN5F0JhstsZdnwl0ZHbTCvtWNzuZCTFAu8kp8F")

    auth4 = OAuth1("eOu9N3i8MtHU5eWhzmY4rAFhB",
                   "lV7WCpcilTASdVEI6LSEc5xr4gMWq1IfrzENL1nRKcH6qfYoAB",
                   "27243865-qfLCUXfTsW0seTABz3nVCbZUVNyrdc9IvGyL4guCi",
                   "3OnKOfVlTO3mTa9qiTrBSNjqOK0UZI3nxKEA6TfXAEfxZ")

    # Stijn
    auth5 = OAuth1("Q1gCYMbR57XDhVov4bQjyjp3o",
                   "13xqHLwv8X8Mb8TlHpHJFeUnJLAgI9VSHvgC7MKVr6unIomKE8",
                   "705002686626844673-MzplcXKj4MPkKaPYhUgx1Pdk81XlnLa",
                   "DEhSzuydHCbt5kCSkNO1tS164vbQmIvyORQAL9TJDnl9T")

    auth6 = OAuth1("TkL4uUVTyGBlxSIHLW43wRCZ7",
                   "z3jZUfgspzej9NBZP2Ve7VJrLjLEJ1KKeETYobGcjlfTI8Qc1s",
                   "318980277-a0VWqZIyvLKPqMZzlOnQ2dh9br9bNQWv2fa9uKJm",
                   "hAhUqGgsINIUUxDFa103CW5kD8TDnKEtvR5TsjnkOq6G5")

    return [auth4, auth5, auth6, auth1, auth2, auth3]


if __name__ == '__main__':
    with open("output_files/autoselected_users.pickle", "rb") as file:
        users = pickle.load(file)
        main(users)

