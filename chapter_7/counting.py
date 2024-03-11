current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

current_number = 0
while current_number < 10:
    current_number += 1
    # if a number is even, we go back to the start
    if current_number % 2 == 0:
        continue
    print(current_number)