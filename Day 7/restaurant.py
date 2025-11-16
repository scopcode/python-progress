class Restaurant():

    def __init__(restaurant , name, cuisine):
        restaurant.name = name 
        restaurant.cuisine = cuisine
    
    def describe_restaurant(restaurant):
        print("The restaurant's name is " + restaurant.name.title() + "," + 
              " And the type of cuisine served is " + restaurant.cuisine.title() + " .")

    def open_restaurant(restaurant): 
        print("The restaurant " + restaurant.name.title() + " with " + 
              restaurant.cuisine.title() + " cuisine is now open!.")

restaurant = Restaurant("tripti", "indian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_1 = Restaurant("santushti","Chinese")
restaurant_2 = Restaurant("dominos", "italian")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()