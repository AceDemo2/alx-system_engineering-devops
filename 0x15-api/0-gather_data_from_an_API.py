#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(url + '/users/' + sys.argv[1]).json()
    tasks = requests.get(url + '/todos', params={'userId':sys.argv[1]}).json()
    name = response.get('name')
    content = []
    for i in tasks:
        if i.get('completed'):
            content.append(i.get('title'))
    print(f'Employee {name} is done with tasks {len(content)}/{len(tasks)}:')
    for j in content:
        print('\t ' + j)

