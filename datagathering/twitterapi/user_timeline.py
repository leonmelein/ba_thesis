import requests
from datagathering.twitterapi import ratelimiting


def request(userid, available_tokens, page, debug=False):
    """
    HTTP GET request to gather 200 of the latest posts of a particular user.

    :param userid: the user id of a Twitter user (Int).
    :param available_tokens: unexhausted OAuth1 token objects (List).
    :param page: indicating which part of the users posts to get (Int, e.g. page 2 equals post 201 to 400)
    :param debug: Bool to trigger printing debugging information (default: False)
    :return: in case of a successful request, a Tuple containing the response as String, the available tokens as List.
      In case the request was not successful and the token was not exhausted, the response will be None.
    """

    # Setup URL for request
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    payload = {'user_id': userid, 'count': 200, 'page': page}

    # Perform API request
    r = requests.get(url, auth=available_tokens[0], params=payload)

    # Check if our request was successful
    status, available_tokens = ratelimiting.handle_response(r, available_tokens, debug)

    # If status is true, we got an HTTP 200 and can return the response
    if status:
        return r.text, available_tokens

    # If the status is false, our authentication token was exhausted and thus had an HTTP 429 response.
    # A new key is taken from the pool and the request is repeated.
    elif status == False:
        return request(userid, available_tokens, page, debug)

    # If the status is none, the request failed for some other reason (like HTTP 404).
    # Notify that there was no response by sending None.
    else:
        return None, available_tokens
