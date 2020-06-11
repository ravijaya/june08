from pslogconfig import logger
from time import sleep

if __name__ == '__main__':
    for item in range(1, 11):
        logger.debug(f'the dummy content: {item}')
        sleep(.5)