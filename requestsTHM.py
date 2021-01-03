#!/usr/bin/python3

import requests

session = requests.Session()
url = 'http://10.10.169.100:3000'
path = '/'
solution = ''

while url == url:
    r = session.get(url + path)
    if r.json()['next'] == 'end':
        break
    else:
        path = '/' + r.json()['next']
        solution += r.json()['value']
        print(solution)
