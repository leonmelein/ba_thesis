from datagathering.twitterapi import authentication


def handle_response(api_request, available_tokens, debug=False):
    """
    Handles rate limits of Twitter REST API.
    :return: Tuple with status and available, unexhausted OAuth1 tokens. Status is described as True (request succeeded),
    False (request failed) or None (used OAuth 1 token is exhausted, retry request with unexhasuted token)
    """

    if api_request.status_code == 200:
        if debug:
            try:
                print("There are", api_request.headers['x-rate-limit-remaining'],
                      "remaining on this token in a 15 minute window.")
            except KeyError:
                pass
        return True, available_tokens

    # Handling rate limit by removing exhasted key from pool
    elif api_request.status_code == 429:
        available_tokens.pop(0)

        # If all keys are removed from pool, regenerate the pool
        if not available_tokens:
            available_tokens = authentication.authenticate()

        return False, available_tokens

    else:
        return None, available_tokens
