"""minimal unix alike grep cmd"""
import re


def grep_me(pattern, *args):
    """log parser"""

    for filename in args:
        for line in open(filename):
            if re.search(pattern, line, re.I):
                print(f'{filename}:{line}', end='')


if __name__ == '__main__':
    print('#' * 22)
    grep_me('bash$', '/etc/passwd', '/etc/group', 'passwd.txt')
