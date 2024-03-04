# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

available_toppings = ['mushrooms', 'olives', 'green pepper', 'pepperoni', 
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'extra cheese', 'french fries', 'green pepper']

#if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# Using a for loop to iterate while printing within a list

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")


print("\nFinished making your pizza!")