with open("pi_million_digits.txt") as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line

birthdate = input("Enter Your Birthdate : ")

if birthdate in pi_string:
    print("Birthdate is present")
else:
    print("Not Present!")