age = ""

prompt = "\nPlease enter the age of who will be watching."
prompt += "\n(Enter 'quit' when done.) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 13:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")