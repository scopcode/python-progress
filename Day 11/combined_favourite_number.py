import json

filename = "combined favourite_number.json"
try:
    with open(filename) as file_object:
        favourite_number = json.load(file_object)

except FileNotFoundError:    
    numbers = input("Enter your favourite number :")

    with open(filename, "w") as file_object:
        json.dump(numbers,file_object)
    
   
else:
    print("Your favourite number is " + str(favourite_number))

