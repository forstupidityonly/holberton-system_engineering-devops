#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    emp = requests.get(user_url).json()
    emp_name = emp.get('name')
    emp_id = emp.get('id')
    tasks = requests.get(user_todo).json()
    csv_file = "{}.csv".format(argv[1])

    for task in tasks:
        with open(csv_file, 'a', newline='') as file:
            my_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            vals = []
            vals.append("{}".format(argv[1]))
            vals.append("{}".format(emp_name))
            vals.append("{}".format(task.get('completed')))
            vals.append("{}".format(task.get('title')))
            my_writer.writerow(vals)
