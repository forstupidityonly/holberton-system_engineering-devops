#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list"""
from sys import argv
import requests

if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user_todo ='https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    emp = requests.get(user_url).json()
    emp_name = emp.get('name')
    completed = []
    tasks = requests.get(user_todo).json()
    for task in tasks:
        if task.get('completed') is True:
            completed.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(emp_name,
                            len(completed), len(tasks)))
    if len(completed) > 0:
        for task in completed:
            print("\t {}".format(task))

