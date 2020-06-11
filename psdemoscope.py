"""demo for the scope"""

n = 100  # global


def demo():
    # pm = 'pip'
    n = 'pip'  # local
    print(n)


demo()
print(n)
