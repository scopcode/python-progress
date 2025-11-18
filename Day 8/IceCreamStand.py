class Restaurant():

    def __init__(self , name, cuisine):
        self.name = name 
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print("The restaurant's name is " + self.name.title() + "," + 
              " And the type of cuisine served is " + self.cuisine.title() + " .")

    def open_restaurant(self): 
        print("The restaurant " + self.name.title() + " with " + 
              self.cuisine.title() + " cuisine is now open!.")
        
class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine,flavours):
        super().__init__(name, cuisine)
        self.flavours = flavours

    def display_flavour(self):
        print(self.flavours)

        

my_icecream = IceCreamStand("Baskin-Robbins", "Dessert" , ["Chocolate", "Vanila", 
                                                           "Strawberry"])
my_icecream.display_flavour()