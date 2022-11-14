#!/usr/bin/python3
"""This records all tasks from employees"""

import json
import requests


def client_request(path, query_string=None):
    """This exports data in json format"""
    url = "https://jsonplaceholder.typicode.com/"
    url += path
    if query_string:
        url = url + "?" + query_string[0] + "=" + query_string[1]

    response = requests.get(url)
    response = response.json()

    return response


if __name__ == "__main__":
    all_users = client_request('users')
    all_todos = client_request('todos')

    data = {}
    for user in all_users:
        user_id = user.get('id')
        data[user_id] = []
        for task in all_todos:
            data[user_id].append({
                    'username': user['username'],
                    'task': task['title'],
                    'completed': task['completed']})

    file_name = 'todo_all_employees.json'
    with open(file_name, "w", encoding='utf-8') as f:
        json.dump(data, f)
