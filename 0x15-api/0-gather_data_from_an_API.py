#!/usr/bin/python3
"""
1-export_to_CSV Module
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_todo_list(empid):
    """for the TODO list"""
    api_url = "https://jsonplaceholder.typicode.com"

    try:
        res = requests.get(api_url + f"/users/{empid}")
        resdata = res.json()

        empname = resdata.get("name")

        res2 = requests.get(api_url + f"/todos?userId={empid}")
        resdata2 = res2.json()
        dtasks = []
        ttasks = len(resdata2)
        for task in resdata2:
            if task.get("completed"):
                dtasks.append(task)

        print(f"Employee {empname} is done with tasks ({len(dtasks)}/{ttasks}):")
        for task in dtasks:
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

get_todo_list(sys.argv[1])
