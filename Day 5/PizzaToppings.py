prompt = "\n Enter the topping you want to enter in the pizza."
prompt += "\n Enter 'quit' to end the program"
prompt += "\n"
message = ""
while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        break
    print(message.title() + " topping has been added to the pizza.")