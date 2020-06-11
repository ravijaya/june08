"""unix like head and tail cmd"""


class HeadandTail:
    def __init__(self, filename):
        pass

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass


if __name__ == '__main__':
    ht = HeadandTail('/etc/passwd')
    print(ht >> 3)  # the last 3 lines of the file
    print()
    print(ht << 3)  # the first 3 lines of the file (head)
