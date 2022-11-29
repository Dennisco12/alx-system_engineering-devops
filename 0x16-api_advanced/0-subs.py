#!/usr/bin/python3
"""This queries the Reddit API and returns the number of
subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function definition"""
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced-Dennisco12'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    try:
        content = response.json()['data']
        # print(content)
        children = content['children']
        # print(children[0])
        data = children[0]['data']
        # print(data)
        count = data['subreddit_subscribers']
        return count
    except Exception:
        return 0
