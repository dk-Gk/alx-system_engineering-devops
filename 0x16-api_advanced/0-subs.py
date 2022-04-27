#!/usr/bin/python3
"""queries the Reddit API"""

import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    hd = {'User-agent': 'Unix:0-subs:v1'}
    rs = requests.get('http://reddit.com/r/{}/about.json'.format(subreddit),
                            hd=hd)
    if rs.status_code != 200:
        return 0
    return rs.json().get('data', {}).get('subscribers', 0)
