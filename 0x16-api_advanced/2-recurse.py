#!/usr/bin/python3
"""queries the Reddit API"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """return list of all hot posts titles of a subreddit"""
    hd = {'User-agent': 'Unix:0-subs:v1'}
    url = 'http://www.reddit.com/r/{}/hot.json?after={}'
    limit = {'limit': 100}
    rs = requests.get(url.format(subreddit), headers=hd, params=limit)
    if rs.status_code == 200:
        data = rs.json().get('data', {})
        after = data.get('after', 'STOP')
        if after is not None:
            hot_list = hot_list + [post.get('data', {}).get('title')
                                   for post in data.get('children', [])]
            recurse(subreddit, hot_list, aft)
        else:
            after = "STOP"
            return hot_list
    else:
        return None
