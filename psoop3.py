"""
PackageManager

name
version

__init__()
get_info()
"""


class PackageManager:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def get_info(self):
        print('name :', self.name)
        print('version :', self.version)


if __name__ == '__main__':
    pm = PackageManager('pip', '2.2.18')
    pm.get_info()
    print(pm.name)
    print(pm.version)
