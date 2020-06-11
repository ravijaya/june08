class Singleton(type):
    """meta class"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


x = SingletonClass()
y = SingletonClass()
z = SingletonClass()  # sublime singleton, borg's singleton
print(id(x))
print(id(y))

"""
There are numerous use cases for metaclasses. Just to name a few:

logging and profiling
interface checking
registering classes at creation time
automatically adding new methods
automatic property creation
proxies
automatic resource locking/synchronization.
"""