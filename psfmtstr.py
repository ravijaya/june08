"""demo for the formatted strings """

name, age = 'sarah', 3

print('I name, age years old')
print()
print(f'I {name}, {age} years old')  # formatted string
print()
print(f'I {name.title()}, {age * 3} years old')  # formatted string

