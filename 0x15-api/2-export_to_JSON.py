#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import requests
import sys
import json


if __name__ == "__main__":
    id = sys.argv[1]
    js_file = {str(id): []}
    file_name = id + ".json"
    api_url = f"https://jsonplaceholder.typicode.com/todos/"
    api_url2 = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos = requests.get(api_url)
    name = requests.get(api_url2)
    todos = todos.json()
    name = name.json()
    USERNAME = name["username"]

    for i in range(len(todos)):
        if todos[i]["userId"] == int(id):
            js_file[str(id)].append({"task": todos[i]["title"],
                                     "completed": todos[i]["completed"],
                                     "username": USERNAME})

    with open(file_name, 'w') as f:
        json.dump(js_file, f)
