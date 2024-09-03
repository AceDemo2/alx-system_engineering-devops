#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests

def number_of_subscribers(subreddit):
    """Return number of subscribers of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {'User-Agent': 'my-reddit-app'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data['data']['subscribers']
    except (ValueError, KeyError):
        return 0

