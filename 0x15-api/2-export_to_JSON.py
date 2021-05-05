#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    emp = requests.get(user_url).json()
    emp_name = emp.get('username')
    tasks = requests.get(user_todo).json()
    json_file = "{}.json".format(argv[1])
    todo_list = []
    mydict = {}
    with open(json_file, 'w') as f:
        for task in tasks:
            task_dict = {}
            task_dict['username'] = emp_name
            task_dict['task'] = task.get('title')
            task_dict['completed'] = task.get('completed')
            todo_list.append(task_dict)
        mydict[argv[1]] = todo_list
        json.dump(mydict, f, indent=2)
