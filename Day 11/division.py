print("Give me two number and I'll divide them.")
print("Press 'q' to quit.")

while True :
    first_number = int(input("First number : "))
    if first_number == 'q':
        break
    second_number = int(input("Second number : "))
    if second_number == 'q':
        break
    try:
        answer = first_number/second_number
    except ZeroDivisionError:
        print("You cannot divide by Zero.")
    else:
        print(int(answer))

