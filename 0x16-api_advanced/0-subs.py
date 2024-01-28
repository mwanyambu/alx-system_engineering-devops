#!/usr/bin/python3

"""
script returns the number of subscribers from querried reddit api
"""


import requests


def number_of_subscribers(subreddit):
    """function querries reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers={"User-Agent": "My reddit api 1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        subs = data.get('subscribers', 0)
        return susbs
    else:
        return 0
