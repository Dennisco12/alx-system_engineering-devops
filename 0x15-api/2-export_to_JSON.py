#!/usr/bin/python3
"""This exports data in the CSV format"""

import json
import requests
import sys


def client_request(data, query_string=None):
    """This returns data from the url in json format"""
    url = 'https://jsonplaceholder.typicode.com/'

    # Add file path and query string to url
    url += data
    url = url + "?" + query_string[0] + "=" + query_string[1]

    # get data from the url
    response = requests.get(url)

    # convert data to json format
    response = response.json()
    return response


if __name__ == "__main__":
    user_id = sys.argv[1]
    users = client_request('users', ('id', user_id))[0]
    tasks_available = client_request("todos", ("userId", user_id))

    file_name = user_id + ".json"
    user_data = users['id']
    data = {user_data: []}

    for task in tasks_available:
        data[user_data].append({'task': task['title'],
                                'completed': task['completed'],
                                'username': users['username']})

    with open(file_name, "w", encoding='utf-8') as f:
        json.dump(data, f)
