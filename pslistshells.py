from csv import reader
from collections import Counter as C
from pprint import pprint as pp

shells = {row[-1] for row in reader(open('/etc/passwd'), delimiter=':')}  # set comprehensions
print(shells)
print()

users_shell = [row[-1] for row in
               reader(open('/etc/passwd'), delimiter=':')]  # list comperhension, extract the last column into list
print(users_shell)
print(len(users_shell))
print()

c = C(users_shell)

for shell, count in c.items():
    print(shell, '->', count)

if True:
    n = 'catch22'

print(shell, count)  # symbol table
