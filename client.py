import os
from groupy import Client
from termcolor import colored, cprint


client = Client.from_token(input("Put your Acess Key here: "));
os.system('clear')
groups = list(client.groups.list_all())
commands = ["/g" "/group" "/c" "/chat"]

groups.reverse()

for group in groups:
    cprint(group.name,'cyan')


groupnum = int(input("Which group would you like to read : ")) -1 
os.system('clear')
messages = groups[groupnum].messages.list()
message_list = []



for i in range(20):
    message_list.append(messages[i])

message_list.reverse()
for message in message_list:
    print(colored(message.name + " : ", "cyan") + message.text)

while True:
    message_text = input()
    for command in commands:
        if message_text == command:
            break
        else:
            groups[groupnum].post(text=message_text)

