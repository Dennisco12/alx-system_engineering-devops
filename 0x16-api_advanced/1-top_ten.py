#!/usr/bin/python3
"""This queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Function definition"""
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers={'User-Agent': '0x16-api_advanced-Dennisco12'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("None")
        return

    try:
        my_dict = {}
        content = response.json()
        data = content['data']['children']
        for k in data:
            key = k['data']['title']
            my_dict[key] = k['data']['upvote_ratio']
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
        my_list = []
        for k in sorted_dict:
            my_list.append(k)

        for post in my_list[:10]:
            print(post)
    except Exception as e:
        print(None)
