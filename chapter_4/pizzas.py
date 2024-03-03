pizzas = ['cheese', 'pepperoni', 'sausage']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print(f"\nI like {len(pizzas)} types of pizzas.")

friend_pizzas = pizzas[:]
pizzas.append('ham')
friend_pizzas.append('pineapple')

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")
print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")