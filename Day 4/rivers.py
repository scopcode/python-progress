rivers = {"Nile" : "Egypt",
          "Ganga" : "India",
          "Amazon" : "South America",
          }
for river,country in sorted(rivers.items()):
    print(river + " flows in " + country)
print("\nRivers included in this dictionary: ")
for river in rivers.keys():
    print(river)
print("\nCountries included in this dictionary: ")
for country in rivers.values():
    print(country)