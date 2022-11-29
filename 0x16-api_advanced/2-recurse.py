#!/usr/bin/python3
"""This queries the Reddit API and returns the length of all
hot posts listed for the given subreddit"""

import requests


def recurse(subreddit, hot_list=[], n=0):
    """Function definition"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced-Dennisco12'}
    response = requests.get(url, headers=header)

    if response.status_code != 200:
        return

    my_list = []
    data = response.json()['data']['children']
    if len(data) == 0:
        return

    m = n + 1
    if m > len(data):
        return hot_list
    hot_list.append(data[n]['data']['title'])
    n += 1
    return recurse(subreddit, hot_list, n)
