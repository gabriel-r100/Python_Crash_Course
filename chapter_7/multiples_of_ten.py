number = input("Give me a number and I'll verify if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is not a multiple of 10.")