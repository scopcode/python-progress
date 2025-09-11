tomy = {"species" : "dog",
        "age" : "10",
        "owner" : "elon musk",
        }
billi = {"species" : "cat",
        "age" : "5",
        "owner" : "taylor swift",
        }
budgie = {"species" : "parrot",
        "age" : "10",
        "owner" : "shubham choubey",
        }
pets = [tomy, billi, budgie]
pet_name = ["tomy", "billi", "budgie"]
x = 0 
for pet in pets:
    print(pet_name[x].title())
    for key,value in pet.items():
        print(key.title() + " - " + str(value.title()))
    print("\n")
    x = x+1