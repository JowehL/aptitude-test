def exercise():
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number:"))
    smallest_number = min(first_number, second_number)
    highest_number = max(first_number, second_number)
    
    for i in range(10):
        if (i % smallest_number == 0 and i % highest_number == 0):
            print("HANS DEKKER")
        elif (i % smallest_number == 0):
            print("HANS")
        elif (i % highest_number):
            print("DEKKER")
        else:
            print(i)

exercise()
