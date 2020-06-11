# import sys
# sys.path.append('/tmp')


import pslogparser


if __name__ == '__main__':
    pslogparser.grep_me('bash$', '/etc/passwd')
    print(__name__)
    print(pslogparser.__name__)
