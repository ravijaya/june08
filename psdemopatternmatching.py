import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy match

m = re.search(pattern, s, re.I)

if m:
    print('match string :', m.group())
    print(m.span(), m.start(), m.end())
else:
    print('failed to match....')


