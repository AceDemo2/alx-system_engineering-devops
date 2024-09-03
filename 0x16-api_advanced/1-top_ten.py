#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return  # Exit early if invalid input

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json()
        my_data = results.get('data', {}).get('children', [])

        if not my_data:
            print("None")
            return

        for i in my_data:
            print(i.get('data', {}).get('title'))

    except ValueError:  # JSON decoding can fail
        print("None")
    except Exception:  # Catch-all for any other exceptions
        print("None")

