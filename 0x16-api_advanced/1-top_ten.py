#!/usr/bin/python3

"""
script returns the number of subscribers from querried reddit api
"""


import requests


def top_ten(subreddit):
    """function querries reddit api"""
    try:
        response = requests.get(
                "https://www.reddit.com/r/{}/hot.json".format(subreddit),
                headers={"User-Agent": "my-reddit-app/1.0"},
                allow_redirects=False,
                params={'limit': 10},
        )
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for x in range(10):
                print(children[x].get('data').get('title'))
        else:
            print(None)
    except Exception:
        print("None")
