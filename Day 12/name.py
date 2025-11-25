from name_function import get_formatted_name

print("Enter 'q' to exit.")

while True:
    first = input("Enter you first name : ")
    if first == 'q':
        break
    last = input("Enter you last name : ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first,last)
    print("\nNeatly formatted name is : " + formatted_name + ".")