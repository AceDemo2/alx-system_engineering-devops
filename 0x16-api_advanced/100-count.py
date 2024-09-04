#!/usr/bin/python3
""" raddit api"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """count all words"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    head = {'User-Agent': 'law'}
    params = {'after': after}
    res = requests.get(url, headers=head, params=params, allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json()['data']
    after = data['after']
    ch = data['children']
    if not counts:
        counts = {}
        for i in word_list:
            counts[i.lower()] = 0
    for j in ch:
        title = j['data']['title'].lower()
        for k in word_list:
            if k in title.lower():
                counts[k] += title.count(k)
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sc = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for i, j in sc:
            if j > 0:
                print(f'{i}: {j}')

