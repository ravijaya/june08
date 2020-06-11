items = [1, 3, 2, 4, 5, 6, 7]
temp1 = [i ** i for i in items]
print(temp1)
print()

temp2 = [i for i in items]
print(temp2)
print()

temp3 = [i for i in items if i % 2]   # compound list comprehension
print(temp3)
print()
