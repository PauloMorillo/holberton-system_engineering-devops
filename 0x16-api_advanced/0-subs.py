#!/usr/bin/python3
""" this module get data from a reddit API """

import requests


def number_of_subscribers(subreddit):
    """ This function get data from API """
    ans = requests.get("https://www.reddit.com/r/" + subreddit + ".json",
                       headers={'user-agent': 'X-Modhash'})
    # print(ans.json())
    try:
        lis = ans.json()["data"]["children"]
        return(lis[0]["data"]["subreddit_subscribers"])
        # return(lis)
    except:
        return(0)
