places_to_visit = ['South Korea', 'Germany', 'England', 'Canada', 'Finland']
print(places_to_visit)

print("\nThis is the sorted list:")
print(sorted(places_to_visit))

print("\nThis is the original list:")
print(places_to_visit)

print("\nThis is a reverse sorted list:")
print(sorted(places_to_visit, reverse=True))

print("\nThis is the original list:")
print(places_to_visit)

print("\nThis is the original list reversed:")
places_to_visit.reverse()
print(places_to_visit)

print("\nThis is the original list reversed again (back to normal):")
places_to_visit.reverse()
print(places_to_visit)

print("\nThis is a permanently sorted list:")
places_to_visit.sort()
print(places_to_visit)

print("\nThis is a permanently sorted list reversed:")
places_to_visit.sort(reverse=True)
print(places_to_visit)