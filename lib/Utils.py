import json
import os
import requests
from getpass import getpass
from bs4 import BeautifulSoup

def get_session_cookie():
    sesh = requests.session()
    ans = sesh.get('https://cv-gml.ru/login')
    soup = BeautifulSoup(ans.text, "html.parser")
    csrf_token = soup.find(id='csrf_token')['value']
    ans = sesh.post("https://cv-gml.ru/login", 
                    data={'email':input('Enter email: '), 
                        'password':getpass('Enter password: '), 
                        'csrf_token': csrf_token})

    if ans.status_code != 200 or 'Неправильный логин или пароль' in ans.text:
        print('Error! Login failed')
        exit(1)
    
    return sesh.cookies['session']

def get_headers():
    if os.path.exists('headers.txt'):
        with open('headers.txt', 'r') as cookie:
            headers = json.loads(cookie.read().replace("'", '"'))
        return headers
    else:
        login_bool = input('No headers file found. Login from terminal? [Y/n] ').lower()
        while login_bool not in ('', 'n', 'y'):
            login_bool = input('Login from terminal? [Y/n] ')

        if login_bool == 'n':
            exit(0)

    headers = login()
    print()
    return headers

def login():
    with open('default_headers.txt', 'r') as cookie:
        headers = json.loads(cookie.read().replace("'", '"'))
    headers['Cookie'] = f'session={get_session_cookie()}'

    with open('headers.txt', 'w') as cookie:
        cookie.write(json.dumps(headers, indent=4))
    
    return headers