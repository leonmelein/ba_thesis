import pickle
import requests
import json
from requests_oauthlib import OAuth1

def main(users):
    applicable_users = {}
    available_auths = getAuth()

    flattened_values = list(users.keys())
    chunks = get_chunks(flattened_values, 100)
    for chunk in chunks:
        usersids = ",".join(chunk)
        print(usersids)
        info, available_auths = request(usersids, available_auths)

        counts = json.loads(info)
        for user in counts:
            userid, count, private = user['id'], user['statuses_count'], user['protected']

            if count > 1000 and private == False:
                applicable_users[userid] = users[str(userid)]

    print("Users:", len(applicable_users.keys()))
    with open("applicable_users.pickle", "wb+") as outputfile:
        pickle.dump(applicable_users, outputfile)


def request(userid, available_auths):
    user_request = request_user_timeline(userid, available_auths)

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


def request_user_timeline(userids, available_auths):
    url = 'https://api.twitter.com/1.1/users/lookup.json'
    r = requests.post(url, auth=available_auths[0], data={"user_id":userids})
    return r


def get_chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))


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

with open("output_files/user_class_income.pickle", "rb") as inputfile:
    userfile = pickle.load(inputfile)
    main(userfile)