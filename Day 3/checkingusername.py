#list of usernames present in the website
current_users = ["iROn123", "p90HAter", "babayaga", "chow", "captaindia"]
#list of new users 
new_users = ["champ123", "iRon123", "p90Hater", "blahhh", "scopcode"]
#looping through new users
for user in new_users:
    #using another loop to access current users to check case senstivity.
    for users in current_users:
        if user.lower() == users.lower():
            print(user + " - Username already exists!.")
    else:
        print("Username available.")
