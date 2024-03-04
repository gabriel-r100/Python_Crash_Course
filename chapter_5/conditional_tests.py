car = 'toyota'

print("Is car == 'toyota'? I predict True.")
print(car == 'toyota')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


pizza = 'sausage'

print("\nIs pizza == 'sausage'? I predict True.")
print(pizza == 'sausage')

print("\nIs pizza == 'pineapple'? I predict False.")
print(pizza == 'pineapple')


donut = 'maple'

print("\nIs donut == 'maple'? I predict True.")
print(donut == 'maple')

print("\nIs donut == 'glazed'? I predict False.")
print(donut == 'glazed')

print("\nIs donut != 'glazed'? I predict True")
print(donut != 'glazed')

tree = '나무'

print("\nIs tree == '나무'? I predict True.")
print(tree == '나무')

print("\nIs tree == '고양이'? I predict False.")
print(tree == '고양이')


age = 21

print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

tested = []
tested.append(car)
tested.append(pizza)
tested.append(donut)
tested.append(tree)
tested.append(age)

if 21 in tested:
    print("21 is in my list of tested variables.")

if 'suburu' not in tested:
    print("'suburu' is not in my list of tested variables.")

print(tested)