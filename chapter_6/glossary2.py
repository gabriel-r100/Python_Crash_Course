glossary = {
    'print()': 'outputs to the terminal',
    '.title()': 'uses title case on a string',
    'for loop': 'iterates through an array',
    'if statements': 'validates a condition',
    'elif statements': 'tests an alternate condition to an if statemen',
    'else': 'when other conditions are not met, this action is performed',
    '.items()': 'used to indicate that both keys and values are going to be used',
    '.keys()': 'used to indicate that only the keys will be looked at',
    '.values()': 'used to indicate that only the values will be looked at',
    'sorted()': 'used to order items alphabetically'
}

for key, value in glossary.items():
    print(f"The definition of {key} is: {value}")