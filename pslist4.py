"""delete by value"""

items = [2.2, 'pam', 4, 5, 3, 'pam', 'pam', .98, 'pam', 'pam', 'pam']
print(items)
print()

item = 'pam'
temp = []

temp = items[:items.index('pam')+1]

for value in items[items.index('pam')+1:]:
    if value != 'pam':
        temp.append(value)



print(temp)
# print(set(items))


