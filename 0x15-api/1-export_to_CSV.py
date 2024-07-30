#!/usr/bin/python3
"""
1-export_to_CSV Module
a Python script that, using this REST API, for a given employee ID,
exports data to csv file
"""
import csv
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
        with open(f"{empid}.csv", 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            for task in resdata2:
                data = [empid, username, task['completed'],
                        task['title']]
                writer.writerow(data)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    get_todo_list(sys.argv[1])
