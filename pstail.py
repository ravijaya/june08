"""
5 lines, last 3

  | | |

l1 |l2|l3

l2 | l3 | l4

l3 | l4 | l5

"""

from collections import deque

for line in deque(open('/etc/passwd'), 3):
    print(line, end='')