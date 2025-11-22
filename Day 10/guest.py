with open("guest.txt", "w") as file_object:
    name = input("Write your name : ")
    file_object.write(name)