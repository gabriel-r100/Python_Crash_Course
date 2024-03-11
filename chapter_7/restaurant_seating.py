group_size = input("How many seats do you need? ")
group_size = int(group_size)

if group_size > 8:
    print("\nPlease wait for a table to become available.")
else:
    print("\nYou table is ready!")