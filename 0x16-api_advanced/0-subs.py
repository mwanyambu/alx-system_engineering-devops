#!/usr/bin/python3

"""
script returns the number of subscribers from querried reddit api
"""


import requests


def number_of_subscribers(subreddit):
    """function querries reddit api"""
    response = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={"User-Agent": "my-reddit-app/1.0"},
    )
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
