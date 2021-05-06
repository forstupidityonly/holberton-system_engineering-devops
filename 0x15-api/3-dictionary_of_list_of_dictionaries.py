#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(user_url).json()
    json_file = 'todo_all_employees.json'
    mydict = {}
    for i in users:
        u_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            i.get('id'))
        emp = i.get('username')
        tasks = requests.get(u_todo).json()
        todo_list = []
        with open(json_file, 'w') as f:
            for task in tasks:
                taks_dict = {}
                taks_dict['username'] = emp
                taks_dict['task'] = task.get('title')
                taks_dict['completed'] = task.get('completed')
                todo_list.append(taks_dict)
            mydict[i.get('id')] = todo_list
            json.dump(mydict, f, indent=2)
