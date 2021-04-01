message = input("Enter your message: ")
new_message = []
split_message = message.split(" ")
for mesg in split_message:
    new_message.append(mesg)

print(new_message)