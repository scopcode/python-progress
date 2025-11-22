with open("guestbook.txt","a") as file_object:
    name = ""
    while name != "quit" :
        name = input("Enter your name : ")
        if name == "quit":
            break
        message = "You're welcome " + name.title() + "\n"
        print(message)
        file_object.write(message)
