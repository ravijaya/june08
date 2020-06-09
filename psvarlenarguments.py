"""variable len arguments """


def demo(*args):
    print(args)


# demo()
# demo(1000)
# demo(1, 2, 'iii', 4, 5)

items = [11, 22, 33]
demo(items)
demo(*items)  # content of the object as arguments
print()

items = (11, 22, 33)
demo(items)
demo(*items)
print()

demo('peter')
demo(*'peter')