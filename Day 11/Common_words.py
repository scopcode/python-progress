filename = "Through the looking glass.txt"
with open(filename, errors = "ignore") as file_object:
    contents = file_object.read()
    words = contents.split()
    word_count = len(words)
    print(word_count)

    occurence_tale = contents.lower().count("tale")
    print(occurence_tale)