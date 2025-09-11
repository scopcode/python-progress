person_1 = {"First Name" : "Shubham",
          "Last Name" : "Choubey",
          "Age" : "29",
          "City" : "Durg",
          }
person_2 = {"First Name" : "Elon",
          "Last Name" : "Musk",
          "Age" : "52",
          "City" : "L.A",
          }
person_3 = {"First Name" : "Vladmir",
          "Last Name" : "Putin",
          "Age" : "55",
          "City" : "Russia",
          }
people = [person_1, person_2, person_3]

for person in people:
    for key,value in person.items():
        print(key + " - " + value )
    print("\n")