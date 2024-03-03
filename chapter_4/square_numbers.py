squares = []
# for value in range(1, 11):
#    square = value ** 2
#    squares.append(square)

# more concisely
# for value in range(1, 11):
#    squares.append(value**2)

# even more concise
squares = [value**2 for value in range(1, 11)]

print(squares)