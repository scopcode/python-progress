def make_sandwich(*fillings) :
    for filling in fillings:
        print(f"Sandwich with {filling.title()} is being prepared.")

make_sandwich("tuna")
make_sandwich("cheese", "bombay masala")