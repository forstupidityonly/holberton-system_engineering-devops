#!/usr/bin/python3
"""get subs"""
import requests


def number_of_subscribers(subreddit):
    """get subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    sub = requests.get(url, headers={"User-Agent": "Custom"})

    if (sub.status_code == 200):
        return sub.json().get("data").get("subscribers")
    else:
        return (0)
