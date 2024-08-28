#!/usr/bin/python3
"""export to csv"""
import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    usrid = sys.argv[1]
    response = requests.get(url + '/users/' + usrid).json()
    tasks = requests.get(url + '/todos', params={'userId': sys.argv[1]}).json()
    name = response.get('username')
    with open(f'{usrid}.csv', 'w') as csvf:
        write = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for task in tasks:
            tstatus = task.get('completed')
            title = task.get('title')
            write.writerow([usrid, name, tstatus, title])
