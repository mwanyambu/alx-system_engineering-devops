#!/usr/bin/python3

"""script gathers data from an API"""

import csv
import json
import requests
import sys

fetch_url = "https://jsonplaceholder.typicode.com"


def find_users():
    """find usernames"""
    response = requests.get("{}/users".format(fetch_url))
    return {user["id"]: user["username"] for user in response.json()}


def to_json(todos, users):
    """all employees todo"""
    info = {}
    for todo in todos:
        user_id = str(todo["userId"])
        username = users.get(int(user_id), "Unknown")
        data = {
                "Username": username,
                "task": todo['title'],
                "completed": todo["completed"],
        }
        if user_id in info:
            info[user_id].append(data)
        else:
            info[user_id] = [data]
    with open("todo_all_employees.json", 'w', encoding='utf-8') as jsonfile:
        json.dump(info, jsonfile, indent=4)


if __name__ == "__main__":
    response = requests.get("{}/todos".format(fetch_url))
    todos = response.json()
    users = find_users()

    to_json(todos, users)
