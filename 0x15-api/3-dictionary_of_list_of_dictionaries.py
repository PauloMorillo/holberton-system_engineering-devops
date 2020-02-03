#!/usr/bin/python3
""" This script get data from an API with ID and send to JSON file """


import json
import requests

if __name__ == "__main__":
    ans2 = requests.get("https://jsonplaceholder.typicode.com/todos/")
    licomplete = []
    idl = 1
    while True:
        for dicto in ans2.json():
            print(dicto)
            id = dicto.get("userId")
            print(id, "and type is ", type(id))
            ans = requests.get("https://jsonplaceholder.typicode.com/users/"+str(id))
            name = ans.json().get("username")
            dictask = {"task": dicto.get("title"),
                       "completed": dicto.get("completed"),
                       "username": name}
            licomplete.append(dictask)
            if idl is not id:
                break
            idl = id
        dictojson = {id: licomplete}
    with open("todo_all_employees.json", 'w', encoding="UTF-8") as jsf:
        json.dump(dictojson, jsf)
