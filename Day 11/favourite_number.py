import json

filename = "favourite_number.json"

numbers = input("Enter your favourite number :")

with open(filename, "w") as file_object:
    json.dump(numbers,file_object)


