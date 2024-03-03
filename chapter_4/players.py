players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

# no start index provided
print(players[:3])
# no stop index provided
print(players[2:])
# negative start index
print(players[-3:])

# looping through a slice
print("Here are the first three players on my team:")

for player in players[:3]:
    print(f"\t{player.title()}")

print(f"The first three items in the list are:\n\t{players[:3]}")
print(f"The middle three items in the list are:\n\t{players[1:4]}")
print(f"The last three items in the list are:\n\t{players[-3:]}")