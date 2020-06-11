import re

pattern = '^r'

matched_lines = filter(lambda line: re.search(pattern, line, re.I), open('passwd.txt'))

for matched_line in matched_lines:
    print(matched_line, end='')
