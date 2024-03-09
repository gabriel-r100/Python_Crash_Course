david = {
    'first_name': 'david',
    'last_name': 'shark',
    'age': 28,
    'city': 'toronto'
    }

molina = {
    'first_name': 'michael',
    'last_name': 'molina',
    'age': 28,
    'city': 'seattle',
}

eric = {
    'first_name': 'eric',
    'last_name': 'azn',
    'age': 22,
    'city': 'new york',
}

people = [david, molina, eric]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"

    print(f"Full name: {full_name.title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")
