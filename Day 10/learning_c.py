with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    replaced = line.replace("Python", "C")
    print(replaced.rstrip())


