#!/usr/bin/python3

"""script gathers data from an API"""

import requests
import sys

fetch_url = "https://jsonplaceholder.typicode.com"
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

    print("Employee {} is done with tasks ({}/{}):".format(
          emp_name, tot_finished, all_tasks))
    for task in finished:
        print("\t{}".format(task))
