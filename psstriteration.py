"""string iteration"""

s = 'this is a sample string in python'
print(s.split())  # str tok
print()
# iterator

for item in s.split():
    print(item)


for temp in s:
    print(temp, '->', ord(temp))