import requests

response = requests.get('http://127.0.0.1:5000/status')
print(response.json())

username = 'Mary2'
password = '123465'

login_data = {
    'username': username,
    'password': password
}
response = requests.post('http://127.0.0.1:5000/login', json=login_data)
print(response.json())

while True:
    text = input()
    data = {
        'username': username,
        'password': password,
        'text': text
    }
    requests.post('http://127.0.0.1:5000/login', json=login_data)
    response = requests.post('http://127.0.0.1:5000/send', json=data)
    print(response.json())
