#!/usr/bin/python3
"""
0-subs Module
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subsecriptions"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    hdrs = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0'}
    try:
        res = requests.get(url, headers=hdrs, allow_redirects=False)
        print(res)
        if res.status_code == 200:
            number_of_subscribers = res.json()['data']['subscribers']
            return number_of_subscribers
        else:
            return 0
    except Exception as ex:
        print(f'Error :: {ex}')
    return 0
