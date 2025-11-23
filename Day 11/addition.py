print("Give me two number and I'll add them.")
print("Press 'q' to quit.")

while True :
    try:
        first_number = int(input("First number : "))
        if first_number == 'q':
            break
        second_number = int(input("Second number : "))
        if second_number == 'q':
            break
        answer = first_number + second_number
    except ValueError:
        print("Please enter a valid number")
    else:
        print(int(answer))

