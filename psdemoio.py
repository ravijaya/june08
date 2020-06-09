"""demo for the IO"""
try:
    1 / 0
    name = input('enter the name :')
    city = input('enter the city :')
    zip_code = int(input('enter the postal code :'))

    print('name :', name)
    print('city :', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as error:
    print(error)
except Exception:  # generic
    print('internal script error')

print('the next statement after try except block')
