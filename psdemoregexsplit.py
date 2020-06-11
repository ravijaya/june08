"""demo for the regex split"""
import re

s = 'root:x,0:0;root /root:/bin/bash'  # hetro delimited content
pattern = '[:,; ]'  # character set , for a character from the give set

items = re.split(pattern, s)
print(items)
