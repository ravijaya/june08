"""delete by value"""

items = [2.2, 'pam', 4, 5, 3, 'allen', 'jack', 4, 5, .98, 'tim', 'patric', 'kim']
numbers, strs = [], []

for item in items:
    if type(item) in [int, float]:
        numbers.append(item)
    elif type(item) is str:   # identity operator is, is not
        strs.append(item)


print(numbers)
print(strs)