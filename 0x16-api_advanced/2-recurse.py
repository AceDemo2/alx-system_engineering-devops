#!/usr/bin/python3
"""
Using reddit's API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returning top ten post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)
    if results.status_code == 200:
        result = results.json()['data']
        after = result['after']
        ch = result['children']
        for i in ch:
            hot_list.extend(i['data']['title'])
        return recurse(subreddit, hot_list, after) if after else hot_list
    else:
        return None
