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

