#!/usr/bin/python3
"""get subs"""
import requests
import sys


def recurse(subreddit, hot_list=[], counter=None):
    """same thing but recursive"""
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    sub = requests.get(url, headers={"User-Agent": "Custom"})

    if (sub.status_code == 200):
        return (hot_list)
    else:
        return (None)
