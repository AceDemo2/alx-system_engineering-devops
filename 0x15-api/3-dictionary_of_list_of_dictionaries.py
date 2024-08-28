#!/usr/bin/python3
"""export to json"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usrid = 1
    dic = {}
    while True:
        response = requests.get(url + '/users/' + str(usrid)).json()
        if not response:
            break
        tasks = requests.get(url + '/todos', params={'userId': usrid}).json()
        name = response.get('username')
        usrtask = []
        for task in tasks:
            tstatus = task.get('completed')
            title = task.get('title')
            usrtask.append(
                    {'username': name,
                        'task': title,
                        'completed': tstatus})
        dic[str(usrid)] = usrtask
        usrid += 1
    with open('todo_all_employees.json', 'w') as jsonf:
        json.dump(dic, jsonf)
