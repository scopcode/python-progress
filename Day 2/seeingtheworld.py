locations = ["Poland", "Thailand", "Russia", "America", "Japan"]
print("These are the locations I'd love to visit")
print(locations)

print("\n Here is the sorted list temporarily")
print(sorted(locations))

print("\n Checking whether list is in original form")
print(locations)

locations.reverse()
print("\n The list has been reversed.")
print(locations)

locations.reverse()
print("\n Reversing the list in the original form")
print(locations)

locations.sort()
print("\n Sorting the list in alphabetical order")
print(locations)

locations.sort(reverse=True)
print("\n Sorting the list in reverse alphabetical order")
print(locations)