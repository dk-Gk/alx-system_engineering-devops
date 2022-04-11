#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress."""

import requests
import sys


NUMBER_OF_DONE_TASKS = TOTAL_NUMBER_OF_TASKS = 0
titles = []

if __name__ == "__main__":
    id = sys.argv[1]
    api_url = f"https://jsonplaceholder.typicode.com/todos/"
    api_url2 = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos = requests.get(api_url)
    name = requests.get(api_url2)
    todos = todos.json()
    name = name.json()
    EMPLOYEE_NAME = name["name"]
    Userid = name["id"]

    for i in range(len(todos)):
        if todos[i][ "userId"] == int(id):
            TOTAL_NUMBER_OF_TASKS += 1
            if todos[i]["completed"] == True:
                NUMBER_OF_DONE_TASKS += 1
                titles.append(todos[i][ "title"])
    print(f"Employee {EMPLOYEE_NAME} is done with tasks", end=" ")
    print(f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})")
    for title in titles:
        print("\t "+ title)
