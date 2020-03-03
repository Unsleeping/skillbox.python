import time
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)
messages = [
     {'username': 'Jack', 'time': time.time(), 'text': 'Hello'},
     {'username': 'Mary', 'time': time.time(), 'text': 'Hi, Jack'},
]
users = {
     # username: password
     "Jack": "Black",
     "Mary": "12345",
}

@app.route("/")
def hello_view():
    return "Hello, User! This is a raw messenger! Soon it will be much more fancy. You can check the <a href=/status>status</a>  of the server to know how many users already have account here and how many messages have written"


@app.route("/status")
def status_view():
    return {
        'status': True,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'users_count': len(users),
        'messages_count': len(messages)
    }


@app.route("/messages")
def messages_view():
    print(request.args)
    after = float(request.args['after'])

    filtered_messages = []
    for message in messages:
        if message['time'] > after:
            filtered_messages.append(message)

    return {'messages': filtered_messages}


@app.route("/send", methods=['POST'])
def send_view():
    """
    :input: {"username": str, "password": str, "text": str}
    :return: {"ok": bool}
    """
    print(request.json)
    username = request.json["username"]
    password = request.json["password"]
    text = request.json["text"]

    if username not in users or users[username] != password:
        return {'ok': False}

    messages.append({'username': username, 'time': time.time(), 'text': text})
    return {'ok': True}


@app.route("/login", methods=['POST'])
def login_view():
    """
    :input: {"username": str, "password": str}
    :return: {"ok": bool}
    """
    print(request.json)
    username = request.json["username"]
    password = request.json["password"]

    if username not in users:
        users[username] = password
        return {'ok': True}

    elif users[username] == password:
        return {'ok': True}
    else:
        return {'ok': False}


if __name__ == '__main__':
    app.run()
