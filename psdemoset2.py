items = {2.2, 'pam', 4, 5, 3, 'allen', 'jack', 4, 5, .98, 'tim', 'patric', 'kim'}
print(items)
print(type(items))
print()

items.add('netscalar')
items.add('gotomeet')
items.add(3.3)
items.add(4.5)
print(items)
print()
items.remove('pam')
items.remove('patric')
items.remove(.98)
print(items)
print()

for item in items:
    print(item)