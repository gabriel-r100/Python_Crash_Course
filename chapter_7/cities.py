prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# no variable to change to False
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}")