#!/usr/bin/python3
"""export to json"""
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usrid = 1
    response = requests.get(url + '/users/' + usrid).json()
    while respose:
        tasks = requests.get(url + '/todos', params={'userId': usrid]}).json()
        name = response.get('username')
        dic = {usrid: []}
        for task in tasks:
            tstatus = task.get('completed')
            title = task.get('title')
            dic[usrid].append(
                    {'username': name
                        'task': title,
                        'completed': tstatus,
                        })
        usrid += 1
    with open(f'{usrid}.json', 'w') as jsonf:
                json.dump(dic, jsonf)
