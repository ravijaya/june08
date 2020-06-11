import logging

fmt_str = '%(created)f:%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(processName)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='error.log', datefmt='%Y-%m-%d %H:%M:%S:%SS')

logging.debug('debugging messages')
logging.info('confirmation notes')
logging.warning('warnings messages')
logging.error('an error information')
logging.critical('panic error')