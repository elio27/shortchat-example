import os
import requests
import json


def send_message(mess):

    with open("token.json", 'r') as token_file:

        token_file_json = json.loads(token_file.read())

        url = 'https://ShortChat.elio27.repl.co/api/chat/post'
        myobj = {"uuid": f"{token_file_json['token']}", "message": f"{mess}"}

        requests.post(url, data=myobj)


if not os.path.exists("token.json"):

    name = str(input("Welcome to ShortChat python script !\nChoose a username : "))
    token_url = f"https://ShortChat.elio27.repl.co/api/gen_token?name={name}"
    token = requests.get(token_url).text

    token_dict = {
        "name": f"{name}",
        "token": f"{token}"
    }

    token_json = json.dumps(token_dict)

    f = open("token.json", 'w')
    f.write(token_json)
    f.close()

while True:
    chat = requests.get("https://ShortChat.elio27.repl.co/api/chat")
    print(chat.text)
    message = input("Send a mesage or refresh with 'enter'.\n>>> ")

    if message:
        send_message(message)
