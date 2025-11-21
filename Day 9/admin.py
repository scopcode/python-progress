class User():

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print("User's name is " + self.first_name.title() + " " + self.last_name.title() + 
              ".")
        print("Age : " + str(self.age))
        print("E-mail : " + self.email)
    
    def greet_user(self):
        print("Welcome " + self.first_name.title() + " " + self.last_name.title() + " ")

    def increment_login_attempts(self):
        self.login_attempts += 1 
    
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, age, email):
                 
        super().__init__(first_name, last_name, age, email)
        
class Privelages():
    def __init__(self, privelages = ["Add a post", "Delete a Post", "Ban a user"]):
        self.privelages = privelages
    
    def show_privelages(self):
        print(self.privelages)


