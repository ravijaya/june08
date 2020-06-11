"""
functional programming

syntax for the lambda
~~~~~~~~~~~~~~~~~~~~~

    lambda arg1, arg2,.....: expression
"""

# lambda functions always passed as a argument to the function.

power = lambda x, n=0: x ** n
print(power)
print()
print(power(2, 3))
print()
print(power(2))
