#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    header = {'User-Agent': 'law'}
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
