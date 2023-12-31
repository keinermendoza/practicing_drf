import requests
import json
from sys import argv, exit
from dotenv import load_dotenv
import os

load_dotenv()
auth_endpoint = 'http://localhost:8000/api/v1/auth/' 

credentials = {
    'username': os.environ.get('username'),
    'password': os.environ.get('password'),
}

auth_response = requests.post(auth_endpoint, credentials)
if auth_response.status_code != 200:
    exit('invalid credentials')

token = auth_response.json()['token']

headers = {
    'Authorization': f"Bearer {token}"
}


'''THIS program is client for the drf api it takes 3 arguments
    1. client.py
    2. verb:  {get, post, put, delete}
    3. product_id: for get an instance, update and delete.
    
    Usage: python client.py get 
    Usage: python client.py delete 2
    '''

def get_id(id):
    '''just convert and input to int or exit'''
    try:
        return int(id)
    except:
        exit(f'id: {id} is not a valid integer')



# body of programm 
if len(argv) == 2:
    endpoint = 'http://localhost:8000/api/v1/products/'
    
    # for handle ListView
    if argv[1] == 'get':

        response = requests.get(endpoint, headers=headers)

    # for create
    elif argv[1] == 'post':
        title = input('title: ')
        content= input('content: ')
        response = requests.post(endpoint, json={'title':title, 'content':content}, headers=headers)

    else:
        exit(f'{argv[1]} is an invalid method')

elif len(argv) == 3:

    product_id = get_id(argv[2])
    endpoint = f'http://localhost:8000/api/v1/products/{product_id}'
    
    if argv[1] == 'get':
        response = requests.get(endpoint, headers=headers)

    elif argv[1] == 'put':
        title = input('title: ')
        content = input('content: ')

        response = requests.put(endpoint, json={'title':title, 'content':content}, headers=headers)
        
    elif argv[1] == 'delete':
        response = requests.delete(endpoint, headers=headers)
        
    else:
        exit(f'{argv[1]} is an invalid method')


else:
    exit('invalid request')

headers = json.dumps(dict(response.headers), indent=2)
print(headers)
try:
    data = json.dumps(response.json(), indent=2)
    print(data)
except:
    print('status code', response.status_code)



