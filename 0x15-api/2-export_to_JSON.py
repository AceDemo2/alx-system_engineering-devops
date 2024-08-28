#!/usr/bin/python3
"""export to json"""
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usrid = sys.argv[1]
    response = requests.get(url + '/users/' + usrid).json()
    tasks = requests.get(url + '/todos', params={'userId': sys.argv[1]}).json()
    name = response.get('username')
    with open(f'{usrid}.json', 'w') as jsonf:
        dic = {usrid: []}
        for task in tasks:
            tstatus = task.get('completed')
            title = task.get('title')
            dic[usrid].append(
                    {'task': title,
                        'completed': tstatus,
                        'username': name})
        json.dump(dic, jsonf)
