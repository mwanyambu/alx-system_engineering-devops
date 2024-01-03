#!/usr/bin/python3

"""script gathers data from an API"""

import csv
import json
import requests
import sys

fetch_url = "https://jsonplaceholder.typicode.com"


def to_json(employee_id, employee_name, todos):
    data = {
            str(employee_id): [
                {
                    "task": todo['title'],
                    "completed": todo["completed"],
                    "Username": employee_name
                }
                for todo in todos
            ]
        }
    filename = "{}.json".format(employee_id)
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    em_id = int(sys.argv[1])
    response = requests.get("{}/todos?userId={}".format(fetch_url, em_id))
    todos = response.json()
    userr = requests.get("{}/users".format(fetch_url))
    users = userr.json()
    emp_name = next((user['name']
                    for user in users if user['id'] == em_id), 'Unknown')
    all_tasks = len(todos)
    finished = [todo['title'] for todo in todos if todo['completed']]
    tot_finished = len(finished)

    to_json(em_id, emp_name, todos)
