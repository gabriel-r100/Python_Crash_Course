usernames = ['gabriel', 'ralph', 'admin', 'eric', 'stephen']

# checks if list is empty
if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, woudl you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
# if list is empty
else:
    print("We need to find more users.")