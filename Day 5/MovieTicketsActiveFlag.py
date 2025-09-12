prompt = "\nEnter Your Age "
prompt += "\nType 'quit' to exit"
prompt += "\n: "
active = True
while active : 
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        value = int(message)
        if value < 3 : 
            print("The Ticket is free!")
        elif value < 12 : 
            print("The Ticket is $10.")
        elif value > 12 :
            print("The Ticket is $15.")
