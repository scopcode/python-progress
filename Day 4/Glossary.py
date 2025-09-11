glossary = {"loop" : "is used in Python to perform repetitive task",
           "conditional" : "is used in Python to perform task based on a condition",
            "list" : "is a data structure in Python that holds values just like a normal list",
             "tupple" : "is a data structure in Python similar to list but cannot be modified",
              "dictionary" : "is a data structure in Python that holds key and their value",
                }
for key,value in glossary.items():
    print(key.title() + " " + value)