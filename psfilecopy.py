"""
file-modes  symbols (text file)    binary-file
read            r                   rb
write           w                   wb
append          a                   ab
"""
from os.path import isfile
from os import unlink

print(isfile('bash-copy'))
print()

with open('/bin/bash', 'rb') as fp, open('bash-copy', 'wb') as fw:
    fw.write(fp.read())

unlink('bash-copy')
print(isfile('bash-copy'))
