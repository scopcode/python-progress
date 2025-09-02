pizzas = ["Pepperoni", "Extraveganza", "Farmhouse"]
friends_pizza = pizzas[:]
pizzas.append("Italian")
friends_pizza.append("Margherita")
for pizza in pizzas:
    print("I like "+ pizza + ".")
for pizza in friends_pizza:
    print("Friend likes "+ pizza + ".")

print("\nI LOVE PIZZA!")