sandwich_orders = ['pastrami', 'blt', 'tuna', 'black forest ham', 'pastrami',
                   'pastrami']
finished_sandwiches = []

# we have run out of pastrami
while 'pastrami' in sandwich_orders:
    print("Sorry, we have run out of pastrami for your order.")
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I finished making your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"We made a {sandwich} sandwich.")