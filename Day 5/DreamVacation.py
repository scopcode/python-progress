favourite_vacations = {}
pollisactive = True
while pollisactive : 
    name = input("\nPlease Enter Your Name : ")
    place = input("Which place would you wish to visit once in life : ")
    favourite_vacations[name] = place
    print("\nThankyou " + name + ". Your response has been recorded.")
    response = ""

    while response != "invalid":
        response = input("\nWould you like to take another poll? (Yes/No) : ")
        if response == "no" or response == "No" :
            pollisactive = False
            response = "invalid"
        elif response == "yes" or response == "Yes" : 
            pollisactive = True
            response = "invalid"
        else :
            print("Invalid Response")
            

print("\n\nThe Polling has been Done!.\n")

for name,place in favourite_vacations.items():
    print(name.title() + " would like to visit " + place.title())


