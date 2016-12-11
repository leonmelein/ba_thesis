import requests
from datagathering.twitterapi import ratelimiting


def request(userids, available_tokens, debug=False):
    """
    HTTP POST request to gather user information of up to 100 users per request.
    :param userids: String of comma separated user id's.
    :param available_tokens: A list of unexhausted OAuth1 token objects.
    :param debug: Bool to trigger printing debugging information (default: False)
    :return:
    """
    url = 'https://api.twitter.com/1.1/users/lookup.json'
    r = requests.post(url, auth=available_tokens[0], data={"user_id": userids})

    status, available_tokens = ratelimiting.handle_response(r, available_tokens, debug)
    if status is True:
        return r.text, available_tokens
    elif status is False:
        return request(userids, available_tokens, debug)
    else:
        return None, available_tokens