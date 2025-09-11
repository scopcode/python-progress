cities = {"delhi" : {"country" : "india",
                     "population" : "34.7 million",
                     "fact" : "It is capital of India",
                     },
          "moscow" : {"country" : "russia",
                     "population" : "13.6 million",
                     "fact" : "It is capital of Russia",
                     },
          "washington d.c." : {"country" : "America",
                     "population" : "0.6 million",
                     "fact" : "It is capital of America ",
                     },
}
for city in cities.keys():
    print(city.title())
    for key,value in cities[city].items():
        if key=="fact":
            print(key.title() + " - " + value)
        else:
            print(key.title() + " - " + value.title())
    print("\n")