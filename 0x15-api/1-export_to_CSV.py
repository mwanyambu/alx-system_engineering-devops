#!/usr/bin/python3

"""script gathers data from an API"""

import csv
import requests
import sys

fetch_url = "https://jsonplaceholder.typicode.com"


def to_csv(employee_id, employee_name, todos):
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        """writer.writeheader()"""
        for todo in todos:
            writer.writerow({
                'USER_ID': str(employee_id),
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': 'True'
                                         if todo['completed'] else 'False',
                'TASK_TITLE': todo['title']
            })


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

    to_csv(em_id, emp_name, todos)
