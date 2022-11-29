#!/usr/bin/python3
"""This queries the Reddit API and prints the titles
of the first 10 hot posts listed for the given subreddit"""

import requests


def top_ten(subreddit):
    """Function definition"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced-Dennisco12'}
    response = requests.get(url, headers=header)

    if response.status_code != 200:
        print(None)
        return

    my_list = []
    for k in response.json()['data']['children']:
        my_list.append(k['data']['title'])

    for item in my_list[:10]:
        print(item)
