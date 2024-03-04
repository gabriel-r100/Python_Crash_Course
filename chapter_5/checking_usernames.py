current_users = ['gabriel', 'ralph', 'victoria', 'eric', 'stephen']
new_users = ['david', 'michael', 'gabriel', 'stephen', 'marina']

for user in new_users:
    if user in current_users:
        print("This username is unavailable.")
    else:
        print(f"Username {user} created.")