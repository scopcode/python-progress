def read_contents(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.strip())

cats = read_contents("cats.txt")
dinosaur = read_contents("dinosaur.txt")
dogs = read_contents("dogs.txt")
