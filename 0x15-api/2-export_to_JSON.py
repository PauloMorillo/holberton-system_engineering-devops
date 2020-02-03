#!/usr/bin/python3
""" This script get data from an API with ID and send to JSON file """


import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    ans = requests.get("https://jsonplaceholder.typicode.com/users/"+id)
    name = ans.json().get("username")
    ans2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" +
                        id)
    alltask = len(ans2.json())
    licomplete = []
    for dicto in ans2.json():
        # print(dicto)
            # print(dicto)
        dictask = {"task": dicto.get("title"),
                   "completed": dicto.get("completed"),
                   "username": name}
        licomplete.append(dictask)
    # print("Employee {} is done with tasks({}/{}):".format(name,
    # len(licomplete),
    # alltask))
    # for title in licomplete:
    # print("\b {}".format(title))
    dictojson = {id: licomplete}
    with open(id + ".json", 'w', encoding="UTF-8") as jsf:
        json.dump(dictojson, jsf)
