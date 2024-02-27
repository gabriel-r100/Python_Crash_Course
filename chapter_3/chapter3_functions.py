instruments = ['trombone', 'tuba']

instruments.append('french horn')
instruments.insert(2, 'oboe')
instruments.pop()
instruments.remove('tuba')
instruments.append('tuba')
instruments.pop(1)

instruments.sort()
instruments_reverse = sorted(instruments)

print(instruments)
print(instruments_reverse)

