class User():

    def __init__(user, first_name, last_name, age, email):
        user.first_name = first_name
        user.last_name = last_name
        user.age = age
        user.email = email
        user.login_attempts = 0
    
    def describe_user(user):
        print("User's name is " + user.first_name.title() + " " + user.last_name.title() + 
              ".")
        print("Age : " + str(user.age))
        print("E-mail : " + user.email)
    
    def greet_user(user):
        print("Welcome " + user.first_name.title() + " " + user.last_name.title() + " ")

    def increment_login_attempts(user):
        user.login_attempts += 1 
    
    def reset_login_attempts(user):
        user.login_attempts = 0


user_shubham = User("shubham" , "choubey", 30, "shubham76@amityonline.com")
user_shubham.describe_user()
user_shubham.greet_user()
user_shubham.increment_login_attempts()
user_shubham.increment_login_attempts()
user_shubham.increment_login_attempts()
user_shubham.increment_login_attempts()
print("Total login attempts : " + str(user_shubham.login_attempts))
print("Resetting login attempts.")
user_shubham.reset_login_attempts()
print("Total login attempts : " + str(user_shubham.login_attempts))