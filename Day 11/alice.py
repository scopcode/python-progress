file_name = "alice.txt"
try:
    with open(file_name) as file_object:
        contents = file_name.read()
        print(contents)
except:
    print(file_name + " doesn't exist")