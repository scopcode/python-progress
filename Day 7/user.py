class User():

    def __init__(user, first_name, last_name, age, email):
        user.first_name = first_name
        user.last_name = last_name
        user.age = age
        user.email = email
    
    def describe_user(user):
        print("User's name is " + user.first_name.title() + " " + user.last_name.title() + 
              ".")
        print("Age : " + str(user.age))
        print("E-mail : " + user.email)
    
    def greet_user(user):
        print("Welcome " + user.first_name.title() + " " + user.last_name.title() + " ")

user_shubham = User("shubham" , "choubey", 30, "shubham76@amityonline.com")
user_shubham.describe_user()
user_shubham.greet_user()

user_laven = User("laven" , "grover", 30, "lavengrover@gmail.com")
user_laven.describe_user()
user_laven.greet_user()