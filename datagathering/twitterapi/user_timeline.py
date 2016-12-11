import requests
from datagathering.twitterapi import ratelimiting


def request(userid, available_tokens, page, debug=False):
    """
    HTTP GET request to gather 200 of the latest posts of a particular user.
    :param userid: the user id of a Twitter user as an Int.
    :param available_tokens: A list of unexhausted OAuth1 token objects.
    :param page: Int indicating which part of the users posts to get (e.g. page 2 equals post 201 to 400)
    :param debug: Bool to trigger printing debugging information (default: False)
    :return:
    """
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    payload = {'user_id': userid, 'count': 200, 'page': page}
    r = requests.get(url, auth=available_tokens[0], params=payload)

    status, available_tokens = ratelimiting.handle_response(r, available_tokens, debug)
    if status:
        return r.text, available_tokens
    elif status == False:
        return request(userid, available_tokens, page, debug)
    else:
        return None, available_tokens
