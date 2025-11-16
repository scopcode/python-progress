class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name 
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print("The restaurant's name is " + self.name.title() + "," + 
              " And the type of cuisine served is " + self.cuisine.title() + " .")
        print("And the restaurant has served " + str(self.number_served) + " people.")

    def set_number_served(self,number_served):
        self.number_served = number_served


    def open_restaurant(self): 
        print("The restaurant " + self.name.title() + " with " + 
              self.cuisine.title() + " cuisine is now open!.")
    
    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("tripti", "indian")
restaurant.describe_restaurant()
restaurant.number_served = 123
restaurant.describe_restaurant()
restaurant.set_number_served(1234)
restaurant.describe_restaurant()
restaurant.increment_number_served(1)
restaurant.describe_restaurant()