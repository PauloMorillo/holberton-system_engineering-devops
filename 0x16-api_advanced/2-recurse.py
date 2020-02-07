#!/usr/bin/python3
""" this module get data from a reddit API """

import requests


def recurse(subreddit, hot_list=[]):
    """ This function get all data from API with recursion """
    if ":" in subreddit:
        wo = subreddit.split(":")
        urli = "https://www.reddit.com/r/" + wo[0] + ".json?after=" + wo[1]
        ans = requests.get(urli, headers={'user-agent': 'X-Modhash'})
        # print(words)
        # print("por aquí pasé, requestcon after")
    else:
        urli = "https://www.reddit.com/r/" + subreddit + ".json"
        # print(urli)
        ans = requests.get(urli, headers={'user-agent': 'X-Modhash'})
        # print("por aquí pasé, request simple")
    # print(ans.json())
    try:
        # print("llegó al try")
        # print(ans)
        lis = ans.json()["data"]["after"]
        # print(lis)
        conca = hot_list + ans.json()["data"]["children"]
        # print(conca)
        hot_list = conca
        # print(len(hot_list))

        if lis is not None:
            # print("entra al null")
            if ":" in subreddit:
                # print("entra al words")
                url = wo[0] + ":" + lis
            else:
                # print("no words")
                url = subreddit + ":" + lis
            # print(url)
        else:
            return(hot_list)
        # return(lis)
    except:
        return(None)
    return (recurse(url, hot_list))
