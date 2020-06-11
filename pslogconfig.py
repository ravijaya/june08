import logging

logger = logging.getLogger('thinkpad')  # custom logger
logger.setLevel(logging.DEBUG)

fmt_str = '%(created)f:%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(processName)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log?

sh = logging.StreamHandler()  # console
fh = logging.FileHandler('access.log')  # where to log

sh.setFormatter(fmt)
fh.setFormatter(fmt)

logger.addHandler(sh)  # add handlers to the logger
logger.addHandler(fh)

if __name__ == '__main__':
    print(logger)
