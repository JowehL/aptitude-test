class exercise:
    def __init__(self):
        self.first_number = int(input("Enter first number:"))
        self.second_number = int(input("Enter second number:"))
        self.smallest_number = min(self.first_number, self.second_number)
        self.highest_number = max(self.first_number, self.second_number)

        for i in range(10):
            if (i % self.smallest_number == 0 and i % self.highest_number == 0):
                print("HANS DEKKER")
            elif (i % self.smallest_number == 0):
                print("HANS")
            elif (i % self.highest_number):
                print("DEKKER")
            else:
                print(i)

exercise()
