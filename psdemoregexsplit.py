"""demo for the regex split"""
import re

s = 'root:x,0:0;root /root:/bin/bash'  # hetro delimited content
pattern = '[:,; ]'

items = re.split(pattern, s)
print(items)
