items = list(range(1, 201))
print(items)
print()

m = map(lambda n: n % 7 == 0, items)
print(list(m))
print()

m = filter(lambda n: n % 7 == 0, items)
print(m)
print(list(m))
print()
