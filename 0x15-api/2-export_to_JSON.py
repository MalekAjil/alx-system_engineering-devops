#!/usr/bin/python3
"""
2-export_to_JSON Module
a Python script that, using this REST API, for a given employee ID,
exports data to json file
"""
import json
import requests
import sys


def get_todo_list(empid):
    """for the TODO list"""
    api_url = "https://jsonplaceholder.typicode.com"

    try:
        res = requests.get(api_url + f"/users/{empid}")
        resdata = res.json()

        username = resdata.get("username")

        res2 = requests.get(api_url + f"/todos?userId={empid}")
        resdata2 = res2.json()
        with open(f"{empid}.json", 'w', encoding='UTF8', newline='') as f:
            data = []
            for task in resdata2:
                tsk = {"task": task['title'],
                       "completed": task['completed'],
                       "username": username}
                data.append(tsk)
            json.dump({empid: data}, f)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    get_todo_list(sys.argv[1])
