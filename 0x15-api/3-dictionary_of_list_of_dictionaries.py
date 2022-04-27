#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import requests
import json


if __name__ == "__main__":
    js_file = {}
    api_url = f"https://jsonplaceholder.typicode.com/todos/"
    api_url2 = f"https://jsonplaceholder.typicode.com/users/"
    todos = requests.get(api_url)
    name = requests.get(api_url2)
    todos = todos.json()
    name = name.json()

    for n in name:
        ut = [todo for todo in todos
              if todo.get('userId') == n.get('id')]
        ut = [{'username': n.get('username'),
               'task': todo.get('title'),
               'completed': todo.get('completed')}
              for todo in ut]
        js_file[str(n.get('id'))] = ut

    with open('todo_all_employees.json', 'w') as f:
        json.dump(js_file, f)
