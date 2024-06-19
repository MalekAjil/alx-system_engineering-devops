#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """top_ten: prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    hdrs = {'User-Agent': 'python:top_ten:v1.0 (by/u/MalekAjil)'}
    res = requests.get(url, headers=hdrs, allow_redirects=False)
    if res.status_code != 200:
        print(0)
        return
    data = res.json()
    for post in darta['data']['children']:
        print(post['data']['tit;e'])
