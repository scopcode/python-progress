sandwich_orders = ["salami", "chicken", "potato", "pastrami",
                   "bombay masala", "cheese", "pastrami", "italian"]
finished_orders = []

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("We've Ran Out of Pastrami!\n\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(current_sandwich.title() + " Sandwich is being prepared.")
    finished_orders.append(current_sandwich)

print("\n")

for finished_order in finished_orders:
    print(finished_order.title() + " Sandwich was made finished.")

