"""minimal unix alike grep cmd"""
import re


def grep_me(pattern, *args):
    """log parser"""

    for filename in args:
        for line in open(filename):
            if re.search(pattern, line, re.I):
                print(f'{filename}:{line}', end='')


grep_me('bash$', '/etc/passwd', '/etc/group', 'passwd.txt')
