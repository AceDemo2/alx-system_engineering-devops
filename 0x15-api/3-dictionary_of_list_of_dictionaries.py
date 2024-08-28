#!/usr/bin/python3
"""export to json"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usrid = 1
    response = requests.get(url + '/users/' + usrid).json()
    while respose:
        tasks = requests.get(url + '/todos', params={'userId': usrid}).json()
        name = response.get('username')
        dic = {str(usrid): []}
        for task in tasks:
            tstatus = task.get('completed')
            title = task.get('title')
            dic[str(usrid)].append(
                    {'username': name,
                        'task': title,
                        'completed': tstatus,
                        })
        with open(f'{usrid}.json', 'w') as jsonf:
            json.dump(dic, jsonf)
    usrid += 1
