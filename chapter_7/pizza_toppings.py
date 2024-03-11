prompt = "\nPlease enter the toppings you would like on your pizza:"
prompt += "\n(Type 'quit' when you are done adding toppings.) "

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"\nAdding {topping} to your pizza.")