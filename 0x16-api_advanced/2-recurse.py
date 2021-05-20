#!/usr/bin/python3
"""get subs"""
import requests
import sys


def recurse(subreddit, hot_list=[], counter=None):
    """same thing but recursive"""
    parameters = {"limit": 100}
    url = "https://www.reddit.com/r/" + str(subreddit) + "/hot/.json?counter"
    + str(counter)
    sub = requests.get(
        url,
        headers={
            "User-Agent": "Custom"},
        params=parameters,
        allow_redirects=False)
    if (sub.status_code == 200):
        post_list = []
        hot_post = r.json().get("data").get("children")
        for post in hot_post:
            hot_list.append(post.get("data").get("title"))
        counter = (r.json().get("data").get("counter"))
        if counter is None:
            return (hot_list)
        return (recurse(subreddit, hot_list, counter))
    else:
        return (None)
