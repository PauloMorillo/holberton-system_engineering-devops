#!/usr/bin/python3
""" This script get data from an API with ID and send to JSON file """


import json
import requests

if __name__ == "__main__":
    ans = requests.get("https://jsonplaceholder.typicode.com/users/")
    # print(ans.json())
    dicuser = dict()
    for datauser in ans.json():
        dicuser[datauser.get("id")] = datauser.get("username")
    ans2 = requests.get("https://jsonplaceholder.typicode.com/todos/")
    licomplete = []
    idl = ans2.json()[0].get("userId")
    lis = []
    dictojson = dict()
    for dicto in ans2.json():
        # print(dicto)
        id = dicto.get("userId")
        # print(id, "and type is ", type(id))
        dictask = {"task": dicto.get("title"),
                   "completed": dicto.get("completed"),
                   "username": dicuser.get(id)}
        licomplete.append(dictask)
        if idl is not id:
            # print("poer aquí pasé")
            dictojson[idl] = licomplete
            lis.append(dictojson)
            # print(dictojson)
            licomplete = []
        idl = id
    dictojson[idl] = licomplete
    # print(dictojson)
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(dictojson, jsf)
