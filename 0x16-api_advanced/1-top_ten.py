#!/usr/bin/python3
"""queries the Reddit API"""

import requests

def top_ten(subreddit)::
    """prints the titles of the first 10 hot posts listed for a given subreddit"""
    hd = {'User-agent': 'Unix:0-subs:v1'}
    rs = requests.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                      hd=hd)
    if rs.status_code != 200 or not :
        return print("None")
    for p in rs.json().get('data', {}).get('children', {})[0:10]:
        print(post.get('data', {}).get('title'))
