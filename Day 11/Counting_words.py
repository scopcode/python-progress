title = "Alice in Wonderland.txt"
try:
    with open(title, errors = "ignore") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("File named " + title + " doesn't exists.")
else:
    words = contents.split()
    word_count = len(words)
    print("The " + title + " has " + str(word_count) + " words in it.")