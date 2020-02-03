#!/usr/bin/python3
""" This script get data from an API with ID and send to CSV file """


import csv
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
        if dicto.get("completed") is True:
            # print(dicto)
            licomplete.append(dicto.get("title"))
    # print("Employee {} is done with tasks({}/{}):".format(name,
    # len(licomplete),
    # alltask))
    # for title in licomplete:
    # print("\b {}".format(title))

    with open(id + ".csv", 'w', newline="") as csvfile:
        awriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for dicto in ans2.json():
            awriter.writerow([id, name, dicto.get("completed"),
                              dicto.get("title")])
