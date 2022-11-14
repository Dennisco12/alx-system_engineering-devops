#!/usr/bin/python3
"""This use a REST API to return information about an employee TODO list
progress"""

import json
import requests
import sys


def client_request(data, query_string=None):
    """This returns the json representation of the url"""
    url = "https://jsonplaceholder.typicode.com/"
    url += data
    if query_string is not None:
        url = url + "?" +query_string[0] + "=" + query_string[1]

    response = requests.get(url)
    response = response.json()
    return response


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_info = client_request('users', ('id', user_id))
    task_available = client_request('todos', ('userId', user_id))

    task_finished = []
    for task in task_available:
        if task['completed']:
            task_finished.append(task)

    print('Employee {} is done with tasks({}/{}):'.format(user_info[0]['name'],
                                                          len(task_finished),
                                                          len(task_available)))

    for task in task_finished:
        print("\t {}".format(task['title']))
