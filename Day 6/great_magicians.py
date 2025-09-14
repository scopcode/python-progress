def show_magician(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for magician in magicians:
        magician = magician + " The great"
        magicians_name.append(magician)
    return(magicians_name)

magicians_name =[]
magician_name = ["Mandrake", "Dynamo", "David Blaine"]
magicians_name = make_great(magician_name[:])
show_magician(magician_name)
show_magician(magicians_name)