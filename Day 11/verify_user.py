import json

filename = "username.json"

def get_stored_username():
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Enter your username : ")
    with open(filename, "w") as file_object:
        json.dump(username,file_object)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Are you " + username + "?")
        usrinput = input("'Y' for Yes, 'N' for No : ")
        if usrinput.lower() == "n" :
            username = get_new_username()
            print("We'll remember you when comeback " + username + "!")
        else:
            print("Welcome Back! " + username)
            
    else :
        username = get_new_username()
        print("We'll remember you when comeback " + username + "!")

greet_user()
