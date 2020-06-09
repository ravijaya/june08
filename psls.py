"""unix alike ls"""

from os import listdir, getcwd


def ls(*args):
    """variable len argumnets """
    if len(args) == 0:
        args = (getcwd(),)

    for dir_path in args:
        print(dir_path, ':')
        for dir_item in listdir(dir_path):
            if not dir_item.startswith('.'):
                print(dir_item)
        print()


ls()