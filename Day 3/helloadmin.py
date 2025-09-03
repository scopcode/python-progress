users = ["Mary", "Joseph", "Steven", "Harry","Adam","Admin"]
current_users = ["shubham"]
for user in users:
    if user.lower() == "admin":
        print("Hello Admin!, Would you like to see the status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")
if current_users:
    print(str(len(current_users)) + " Users are online.")
else:
    print("None active, we need to find more users.")
