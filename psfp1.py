items = [2, 1, 3, 2, 4, 5, 8]

m = map(bin, items)  # functional programming
print(m)
print()

for item in m:
    print(item)

print()

m = map(ord, 'peter pan')
print(list(m))