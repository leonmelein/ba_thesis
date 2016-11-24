import pickle
import json
import langid
import os
import time

from TwitterSearch import TwitterSearchException
from TwitterSearch import TwitterUserOrder, TwitterSearch


def divide(users, type="twoway"):
    divided = {}

    for userid in users.keys():
        # Flekova et al. Two Way split: low - high
        if type == "twoway":
            income = users[userid][5]
            if income > 34500:
                currentvalue = divided.get("high", [])
                currentvalue.append([userid, users[userid]])
                divided["high"] = currentvalue
            else:
                currentvalue = divided.get("low", [])
                currentvalue.append([userid, users[userid]])
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

    print(divided.keys())
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

with open('output_files/user_class_income.pickle', 'rb') as inputfile:
    user_dict = pickle.load(inputfile)
    divided_dict = divide(user_dict)

with open('output_files/divided_user_class_income.pickle', 'wb+') as outputfile:
    pickle.dump(divided_dict, outputfile)
