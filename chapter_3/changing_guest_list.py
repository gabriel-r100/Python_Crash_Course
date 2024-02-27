guest_list = ['einstein', 'markey', 'david', 'AJ']

print(f"\n{guest_list[0].title()} you are invited to dinner.")
print(f"{guest_list[1].title()} you are invited to dinner.")
print(f"{guest_list[2].title()} you are invited to dinner.")
print(f"{guest_list[3]} you are invited to dinner.")

declined_invitation = guest_list.pop(1)
print(f'\n{declined_invitation.title()} could not make the dinner.')

guest_list.insert(1, 'eric')
print(f"\n{guest_list[0].title()} you are invited to dinner.")
print(f"{guest_list[1].title()} you are invited to dinner.")
print(f"{guest_list[2].title()} you are invited to dinner.")
print(f"{guest_list[3]} you are invited to dinner.")

print("\nWe have found a bigger table and will be inviting more guests.")
guest_list.insert(0, 'victoria')
guest_list.insert(2, 'omar')
guest_list.append('tori')

print(f"\n{guest_list[0].title()} you are invited to dinner.")
print(f"{guest_list[1].title()} you are invited to dinner.")
print(f"{guest_list[2].title()} you are invited to dinner.")
print(f"{guest_list[3].title()} you are invited to dinner.")
print(f"{guest_list[4].title()} you are invited to dinner.")
print(f"{guest_list[5]} you are invited to dinner.")
print(f"{guest_list[6].title()} you are invited to dinner.")

print("\nUnfortunately, the table will not be arriving in time, we will only have space for two guests.")
uninvited = guest_list.pop()
print(f"Sorry {uninvited.title()}, I am withdrawing the invitation.")
uninvited = guest_list.pop()
print(f"Sorry {uninvited.title()}, I am withdrawing the invitation.")
uninvited = guest_list.pop()
print(f"Sorry {uninvited.title()}, I am withdrawing the invitation.")
uninvited = guest_list.pop()
print(f"Sorry {uninvited.title()}, I am withdrawing the invitation.")
uninvited = guest_list.pop()
print(f"Sorry {uninvited.title()}, I am withdrawing the invitation.")
print(f"\n{guest_list[0].title()} you are invited to dinner.")
print(f"{guest_list[1].title()} you are invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)

print(len(guest_list))