items = [11, 22, 33]

# python's iterable should iterator protocol

items = dict(lang='perl', author='larry', release='parrot')

for item in items:
    print(item)

print()
li = iter(items)
print(li)
# print()
# print(next(li))
# print(next(li))
# print(next(li))
# print(next(li))