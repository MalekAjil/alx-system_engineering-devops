#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subsecriptions"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    hdrs = {'User-Agent': 'custom user-agent'}
    try:
        res = requests.get(url, headers=hdrs, allow_redirections=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except Exception as ex:
        print(f'Error :: {ex}')
    return 0
