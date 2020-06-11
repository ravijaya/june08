# from socketserver import ThreadingTCPServer

class Alpha:
    def pprint(self):
        print('pprint from the class Alpha')


class Beta:
    def pprint(self):
        print('pprint from the class Beta')


class Charlie(Beta, Alpha):
    def pprint(self):
        Alpha.pprint(self)
        Beta.pprint(self)


if __name__ == '__main__':
    Charlie().pprint()


"""factory method"""