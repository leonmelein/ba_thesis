from requests_oauthlib import OAuth1
import json


def authenticate(authentication_file="private/credentials.json"):
    """
    Provides OAuth1 authentication for use with Twitter REST API.
    :param authentication_file: path to JSON file containing Twitter credentials in a JSON Array, with each individual
     set in an Object. See private/example_credentials.json for an example (String, default: private/credentials.json).
    :return: List of OAuth1 token objects for user with the Requests Python Library.
    """

    with open(authentication_file) as inputfile:
        auths = json.load(inputfile)

    oauths = []
    for auth in auths:
        oauth = OAuth1(
            auth["consumer"], auth["consumer_secret"], auth["access"], auth["access_secret"]
        )
        oauths.append(oauth)

    return oauths
