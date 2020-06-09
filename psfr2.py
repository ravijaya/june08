"""pythonic way of file read, context manager"""

with open('/home/ravijaya/Trainings/Python-Citrix/june08/passwd.txt') as fp:
    for temp in fp:
         print(temp, end='')
#     print(fp.closed)
#
# print(fp.closed)

