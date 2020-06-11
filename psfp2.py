"""
112
<ascii char="p">112</ascii>
"""

ascii_values = [112, 101, 116, 101, 114, 32, 112, 97, 110]


def tag_it(av):
    """named function"""
    return f'<ascii char="{chr(av)}">{av}</ascii>'


tags = map(tag_it, ascii_values)
tags = map(lambda av: f'<ascii char="{chr(av)}">{av}</ascii>', ascii_values)  # anon function

for tag in tags:
    print(tag)
