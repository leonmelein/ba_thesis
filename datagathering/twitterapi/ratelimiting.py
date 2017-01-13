from datagathering.twitterapi import authentication


def handle_response(api_request, available_tokens, debug=False):
    """
    Handles rate limits of Twitter REST API.

    :param api_request:
    :param available_tokens:
    :param debug:
    :return: Tuple with status and a List of available, unexhausted OAuth1 tokens.
    Status is described as True (request succeeded),
    False (request failed) or None (used OAuth 1 token is exhausted, retry request with unexhausted token)
    """

    # HTTP 200: we got a proper response to our API request, continue
    if api_request.status_code == 200:
        if debug:
            try:
                print("There are", api_request.headers['x-rate-limit-remaining'],
                      "remaining on this token in a 15 minute window.")
            except KeyError:
                pass
        return True, available_tokens

    # HTTP 429: our OAuth token is exhausted
    # Handling rate limit by removing exhausted key from pool
    elif api_request.status_code == 429:
        available_tokens.pop(0)

        # If all keys are removed from pool, regenerate the pool
        if not available_tokens:
            available_tokens = authentication.authenticate()

        return False, available_tokens

    # A different HTTP status code, like HTTP 404
    # Notify that there was no content returned, but the token isn't exhausted
    else:
        return None, available_tokens
