#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list):
    """a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted
    count of given keywords (case-insensitive, delimited by spaces."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    hdrs = {'User-Agent': 'python:top_ten:v1.0 (by/u/MalekAjil)'}
    res = requests.get(url, headers=hdrs, allow_redirects=False)
    if res.status_code != 200:
        print(0)
        return
    data = res.json()
    for post in darta['data']['children']:
        print(post['data']['tit;e'])
