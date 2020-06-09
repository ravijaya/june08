"""shallow copy vs deep copy"""

items = [11, 22, 33]
temp = items.copy() # backup, clone, deep copy

print(items)
print(temp)
print()

print(items == temp)
print(items is temp)
print(id(temp))
print(id(items))

# s1 = 'Peter'
# s2 = 'PeTer'
# print(s1 == s2)
# print(s1.casefold() == s2.casefold())