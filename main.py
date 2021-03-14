import requests
import os

TOKEN_ENDPOINT = "https://ShortChat.elio27.repl.co/api/gen_token?name="
POST_ENDPOINT = "https://ShortChat.elio27.repl.co/api/chat/post"
READ_ENDPOINT = "https://ShortChat.elio27.repl.co/api/chat"

if not os.path.exists("token.txt"):
	name = input("Welcome to the ShortChat Python script!\nChoose a username: ")
	token_url = TOKEN_ENDPOINT + name
	token = requests.get(token_url).text

	with open("token.txt", "w") as f:
		f.write(token)

with open("token.txt") as token:
	message = ""

	while message != "exit":
		print(requests.get(READ_ENDPOINT).text.strip() + "\n")

		message = input("Send a message or refresh by pressing enter.\n>>> ")

		if message:
			requests.post(POST_ENDPOINT, data = {"uuid": token.read(), "message": message})
		
		os.system("cls" if os.name == "nt" else "clear")
