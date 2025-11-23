def count_words(title):
    try:
        with open(title , errors = "ignore") as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        word_count = len(words)
        print("Total word count in " + title + " is " + str(word_count))

filenames = ["alice in wonderland.txt", "harrpt.txt", "harrypotter.txt", "scopcode.txt"]
for file in filenames:
    count_words(file)