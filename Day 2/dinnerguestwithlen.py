guests = ["Ganesh", "Shiva", "Parwati", "Kartikey"]
message_1 = "Welcome! " + guests[0] + ", You're invited to our dinner."
message_2 = "Welcome! " + guests[1] + ", You're invited to our dinner."
message_3 = "Welcome! " + guests[2] + ", You're invited to our dinner."
message_4 = "Welcome! " + guests[3] + ", You're invited to our dinner."
print(message_1)
print(message_2)
print(message_3)
print(message_4)
length = len(guests)
print("Total number of guests invited to dinner are: " + str(length))
print("\nWe're sorry that our guest Kartikey couldn't make it!")
guests[3] = "Nandi"
message_1 = "\nWelcome! " + guests[0] + ", You're invited to our dinner."
message_2 = "Welcome! " + guests[1] + ", You're invited to our dinner."
message_3 = "Welcome! " + guests[2] + ", You're invited to our dinner."
message_4 = "Welcome! " + guests[3] + ", You're invited to our dinner."
print(message_1)
print(message_2)
print(message_3)
print(message_4)
length = len(guests)
print("Total number of guests invited to dinner are: " + str(length))
print("\n\n Voila! We've just found a bigger dinner table so more guests will be invited!")
guests.insert(0, "Indra")
guests.insert(3, "Laxmi")
guests.append("Brahma")
message_1 = "\nWelcome! " + guests[0] + ", You're invited to our dinner."
message_2 = "Welcome! " + guests[1] + ", You're invited to our dinner."
message_3 = "Welcome! " + guests[2] + ", You're invited to our dinner."
message_4 = "Welcome! " + guests[3] + ", You're invited to our dinner."
message_5 = "Welcome! " + guests[4] + ", You're invited to our dinner."
message_6 = "Welcome! " + guests[5] + ", You're invited to our dinner."
message_7 = "Welcome! " + guests[6] + ", You're invited to out dinner."
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)
print(message_7)
length = len(guests)
print("Total number of guests invited to dinner are: " + str(length))
print("\n Sorry our dinner table couldn't make it in time, and we can only invite two guests.")
popped_guest = guests.pop()
message = ("\nWe're sorry! " + popped_guest + " . We're sorry for the inconvenience caused to you.")
print(message)
popped_guest = guests.pop()
message = ("\nWe're sorry! " + popped_guest + " . We're sorry for the inconvenience caused to you.")
print(message)
popped_guest = guests.pop()
message = ("\nWe're sorry! " + popped_guest + " . We're sorry for the inconvenience caused to you.")
print(message)
popped_guest = guests.pop()
message = ("\nWe're sorry! " + popped_guest + " . We're sorry for the inconvenience caused to you.")
print(message)
popped_guest = guests.pop()
message = ("\nWe're sorry! " + popped_guest + " . We're sorry for the inconvenience caused to you.")
print(message)
message = "\nHello "+ guests[0] + " You're still being invited to our dinner."
message = "\nHello "+ guests[1] + " You're still being invited to our dinner."
length = len(guests)
print("Total number of guests invited to dinner are: " + str(length))
del guests[0]
del guests[0]
print(guests)
length = len(guests)
print("Total number of guests invited to dinner are: " + str(length))
print("Since the list is empty, the dinner has been served!")