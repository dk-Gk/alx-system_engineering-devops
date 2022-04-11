#!/usr/bin/python3
""" Python script to export data in the CSV format"""

import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    file_name = id + ".csv"
    api_url = f"https://jsonplaceholder.typicode.com/todos/"
    api_url2 = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos = requests.get(api_url)
    name = requests.get(api_url2)
    todos = todos.json()
    name = name.json()
    EMPLOYEE_NAME = name["name"]
    USERNAME = name["username"]

    with open(file_name, 'w') as csvfile:
        for i in range(len(todos)):
            if todos[i]["userId"] == int(id):
                csvfile.write('"{}","{}","{}","{}"\n'.format(
                    id, USERNAME, todos[i]["completed"], todos[i]["title"]))
