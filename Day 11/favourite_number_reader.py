import json 

filename = "favourite_number.json"

with open(filename) as file_object:
    favourite_number = json.load(file_object)
    print("Your favourite number is " + str(favourite_number))