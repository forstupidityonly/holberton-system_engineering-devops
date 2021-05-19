#!/usr/bin/python3
"""get subs"""
import requests
import sys


def top_ten(subreddit):
    """top ten post"""
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    sub = requests.get(url, headers={"User-Agent": "Custom"})
    if (sub.status_code == 200):
        val = sub.json().get("data").get("children")
        for post in val:
            my_dict = post["data"]
            print(my_dict.get('title'))
    else:
        print("None")
        return
