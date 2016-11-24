#!/usr/bin/python
import TwitterSearch
import pickle
import os
import json
import random
from TwitterSearch import TwitterSearchException, TwitterUserOrder, TwitterSearch

low = []
high = []


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
    not_a_person, hobby_volunteer, study, wrong_occupation, not_found, not_enough_tweets = 0, 0, 0, 0, 0, 0
    ts = connect_twitter()

    for key in user_dict.keys():
        values = user_dict[key]
        random.shuffle(values)

        i = 0
        while i < 1500:
            item = values[i]

            # Print selection statistics
            print("\n=== Low:", len(low), "High:", len(high), "===")

            # Get user
            twitter_user_order = TwitterUserOrder(int(item[0]))
            try:
                tweets = ts.search_tweets(twitter_user_order)

                # Get number of tweets, disregard users with less than 500 tweets
                no_of_tweets = tweets['content'][000]['user']['statuses_count']
                if no_of_tweets >= 500:

                    # Print user info
                    formatstring = "\nID:\t{}\nReal name:\t{}\nUsername:\t{}\nTweets:\t{}\nDescription:\t{}\nOccupation:\t{}\n"
                    twid, username, real_name, description, occupation = item[0], item[1][0], item[1][1], item[1][2], item[1][3]
                    print(formatstring.format(
                        twid,
                        real_name,
                        username,
                        no_of_tweets,
                        description,
                        occupation
                    ))

                    # Get annotator judgment
                    answer = "a"
                    while answer not in ["y", "n", ""]:
                        print("Is this a real, correctly labeled user?\n[If not: 1 - Not a person; 2 - Hobby/Volunteer; 3 - Study; 4 - Miscellaneous]", end="\n")
                        answer = input()

                    # Process user in accordance with judgment
                    if answer == "":
                        if key == "low":
                            low.append(item)
                        else:
                            high.append(item)
                    else:
                        # try:
                        #     reason = int(answer[1])
                        # except IndexError:
                        #     reason = 1
                        # except ValueError:
                        #     reason = int(answer[2]) # Helping a sleep deprived author...
                        #
                        # while reason not in [1, 2, 3, 4]:
                        #     print("Why is it not?")
                        #     reason = int(input())
                        #
                        # if reason == 1:
                        #     not_a_person += 1
                        # elif reason == 2:
                        #     hobby_volunteer += 1
                        # elif reason == 3:
                        #     study += 1
                        # else:
                        #     wrong_occupation += 1
                        pass
                else:
                    print("User", item[0], "has not enough tweets, skipping")
                    not_enough_tweets += 1

            except TwitterSearchException:
                print("Could not find user", item[0], ", skipping")
                not_found += 1

            except KeyError:
                print("User", item[0], "has no tweets, skipping")
                not_enough_tweets += 1


    # Export selected users to new dictionary
    export_dict = {'low': low, 'high': high}

    # Save selected, divided users
    with open('output_files/selected_divided_users.pickle', 'wb+') as outputfile:
        pickle.dump(export_dict, outputfile)

    # Print outcomes
    print("\nRemaining # of users in high and low class")
    #print("Low:", len(export_dict['low']))
    print("High:", len(export_dict['high']))

    # print("\n\nReasons to exclude users (w/# of users)")
    # print("User")
    print("- User not found:", not_found)
    print("- User does not have enough tweets", not_enough_tweets)
    # print("- User not a person:", not_a_person)
    # print("Occupation")
    # print("- Occupation is hobby/voluntary:", hobby_volunteer)
    # print("- Occupation is study:", study)
    # print("- Occupation is plain wrong:", wrong_occupation)

    print("\nSelection has been saved to disk.")

with open('output_files/divided_user_class_income.pickle', 'rb') as inputfile:
    userdict = pickle.load(inputfile)
    main(userdict)
