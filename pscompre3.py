items = [1, 3, 2, 4, 5, 6, 7]
temp = [bin(i) for i in items]  # list comprehension
print(temp)
print()

items = [1, 3, 2, 4, 5, 6, 7]
temp = {i: bin(i) for i in items}  # dict comprehension
print(temp)
print()

items = [1, 3, 2, 4, 5, 6, 7]
temp = {bin(i) for i in items}  # set comprehension, unordered collection
print(temp)
print()
