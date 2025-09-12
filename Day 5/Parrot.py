prompt = "\n Tell me something, I'll repeat back to you : "
prompt += "\n Enter 'quit' to end the program. "
active = True
while active : 
    message = input(prompt)
    if message == 'quit' :
        active = False
    else : 
        print(message)