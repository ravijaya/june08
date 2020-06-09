items = (2.2, 'pam', 4, 5, 3, 'allen', 'jack', 4, 5, .98, 'tim', 'patric', 'kim')
print(items)
print(type(items))
print(len(items))
print()
# items[-5] = 'five'  # immutable object
print(items[-5])  # indexing
print()

print(items[-5:])  # slice
print()

for item in items[-5:]:
    print(item)