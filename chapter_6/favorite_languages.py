favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")


friends = ['phil', 'sarah']

# loop through favorite_languages and working with keys (names)
for name in favorite_languages:
    print(f"Hi {name.title()}.")

    # if the name is one of our friends, we also run the following script
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# checking if erin took our poll
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

poll_sent = ['phil', 'sarah', 'erin', 'edward', 'jen', 'steph']

for name in poll_sent:
    if name not in favorite_languages.keys():
        print(f"{name.title()}, please respond to our poll.")