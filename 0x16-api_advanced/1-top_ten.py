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
        return

    user_agent = {'User-agent': 'my-reddit-app'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = get(url, headers=user_agent, params=params, allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        # Check if the content type is JSON
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print("None")
            return

        results = response.json()
        my_data = results.get('data', {}).get('children', [])

        if not my_data:
            print("None")
            return

        for post in my_data:
            print(post.get('data', {}).get('title', "None"))

    except Exception as e:
        print("None")

