motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(4, 'kawasaki')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# If motorcycles list stores chronologically, we can use .pop to show the last owned motorcycle
last_owned = motorcycles.pop()
print(f"My last owned motorcycle was a {last_owned.title()}")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')