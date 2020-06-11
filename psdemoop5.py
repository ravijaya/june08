class Demo:
    """don't"""
    def demo(self):
        print('null arguments')

    def demo(self, a, b):
        print(a + b)


if __name__ == '__main__':
    d = Demo()
    d.demo('peter', 'pan')

    n = 12
    n = 13
