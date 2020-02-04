#!/usr/bin/python3
""" This script get data from an API with ID and send to JSON file """


from collections import OrderedDict
import json
import requests

if __name__ == "__main__":
    ans = requests.get("https://jsonplaceholder.typicode.com/users")
    # print(ans.json())
    dicuser = dict()
    dictojson = dict()
    for datauser in ans.json():
        dicuser[datauser.get("id")] = datauser.get("username")
        dictojson[datauser.get("id")] = []
    ans2 = requests.get("https://jsonplaceholder.typicode.com/todos")
    licomplete = []
    idl = ans2.json()[0].get("userId")
    for dicto in ans2.json():
        dictask = OrderedDict()
        # print(dicto)
        id = dicto.get("userId")
        # print(id, "and type is ", type(id))
        dictask["username"] = dicuser.get(id)
        dictask["task"] = dicto.get("title")
        dictask["completed"] = dicto.get("completed")
        dictojson[id].append(dictask)
    with open("todo_all_employees.json", 'w', encoding="UTF-8") as jsf:
        json.dump(dictojson, jsf)
