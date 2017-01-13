import requests
from datagathering.twitterapi import ratelimiting


def request(userids, available_tokens, debug=False):
    """
    HTTP POST request to gather user information of up to 100 users per request.
    :param userids: String of comma separated user id's.
    :param available_tokens: A list of unexhausted OAuth1 token objects.
    :param debug: Bool to trigger printing debugging information (default: False)
    :return: in case of a successful request, a Tuple containing the response as String, the available tokens as List.
      In case the request was not successful and the token was not exhausted, the response will be None.
    """

    # Perform API request
    url = 'https://api.twitter.com/1.1/users/lookup.json'
    r = requests.post(url, auth=available_tokens[0], data={"user_id": userids})

    # Check if our request was successful
    status, available_tokens = ratelimiting.handle_response(r, available_tokens, debug)

    # If status is true, we got an HTTP 200 and can return the response
    if status is True:
        return r.text, available_tokens

    # If the status is false, our authentication token was exhausted and thus had an HTTP 429 response.
    # A new key is taken from the pool and the request is repeated.
    elif status is False:
        return request(userids, available_tokens, debug)

    # If the status is none, the request failed for some other reason (like HTTP 404).
    # Notify that there was no response by sending None.
    else:
        return None, available_tokens