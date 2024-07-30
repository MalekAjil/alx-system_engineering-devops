#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py Module
a Python script that, using this REST API, for a given employee ID,
exports data to json file
"""
import json
import requests
import sys


def get_todo_list():
    """for the TODO list"""
    api_url = "https://jsonplaceholder.typicode.com"

    try:
        res = requests.get(api_url + "/users")
        resdata = res.json()

        data = {}
        for user in resdata:
            userid = user.get("id")
            username = user.get("username")
            res2 = requests.get(api_url + f"/todos?userId={userid}")
            resdata2 = res2.json()

            tasks = []
            for task in resdata2:
                tsk = {"username": username,
                       "task": task['title'],
                       "completed": task['completed']}
                tasks.append(tsk)
            data[userid] = tasks
        with open(f"todo_all_employees.json", 'w', encoding='UTF8') as f:
            json.dump(data, f)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    get_todo_list()
