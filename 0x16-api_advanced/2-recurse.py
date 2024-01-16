#!/usr/bin/python3

""" recursive"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """querry recursively"""
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    children = data.get('children', [])
    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


if __name__ == "__main__":
    subreddit = "programming"
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
