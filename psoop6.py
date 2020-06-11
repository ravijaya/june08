"""accessor pattern"""


class Celsius:
    __temperature = None  # private attribute

    def __init__(self, temperature=0):
        self.temperature = temperature  # setter

    def set_temperature(self, temperature):
        """setter"""
        if temperature < -273.15:
            raise ValueError('Temperature below -273.15 is not possible')

        self.__temperature = temperature

    def get_temperature(self):
        """getter"""
        return self.__temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32  # getter

    temperature = property(get_temperature, set_temperature)   # accessor


if __name__ == '__main__':
    try:
        c = Celsius(37)
        c.temperature = 100
        print(c.to_fahrenheit())
    except ValueError as err:
        print(err)
