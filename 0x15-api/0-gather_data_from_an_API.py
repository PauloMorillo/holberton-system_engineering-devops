#!/usr/bin/python3
""" This script get data from an API with ID """


import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    ans = requests.get("https://jsonplaceholder.typicode.com/users/"+id)
    name = ans.json().get("name")
    ans2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" +
                        id)
    alltask = len(ans2.json())
    licomplete = []
    for dicto in ans2.json():
        # print(dicto)
        if dicto.get("completed") is True:
            # print(dicto)
            licomplete.append(dicto.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(licomplete),
                                                          alltask))
    for title in licomplete:
        print("\b {}".format(title))
