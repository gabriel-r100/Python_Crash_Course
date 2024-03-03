my_foods = ['pizza', 'falafel', 'carrot cake']

# making a copy of my_foods lists
friend_foods = my_foods[:]

# proving they are separate lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)