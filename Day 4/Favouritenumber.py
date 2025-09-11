favourite_numbers = {"Jacob" : ["1", "2" , "3"],
                     "Mary" : ["4", "5", "6"],
                     "Jason" :[ "7", "8", "9"],
                     "Adam" : ["10", "11", "12"],
                     "Alex" : ["13", "14", "15"],
                     }
for name,numbers in favourite_numbers.items():
    print(name.title() + "'s favourite number is : ")
    for number in numbers:
        print(number)
    print("\n")