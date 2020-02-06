#!/usr/bin/python3
""" this module get data from a reddit API """

import requests


def top_ten(subreddit):
    """ This function get data from API """
    ans = requests.get("https://www.reddit.com/r/" + subreddit + ".json",
                       headers={'user-agent': 'X-Modhash'})
    # print(ans.json())
    try:
        lis = ans.json()["data"]["children"]
        if len(lis) >= 10:
            x = 0
            while x < 10:
                print(lis[x]["data"]["title"])
                x = x + 1
        else:
            for x in len(lis):
                print(lis[x]["data"]["title"])
        # return(lis)
    except:
        print(None)
