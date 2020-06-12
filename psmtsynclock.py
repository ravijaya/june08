"""demo for the sync using lock"""

import threading
from time import sleep
from random import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker(delay, lock):
    """thread function"""
    t_id = threading.current_thread().ident
    t_name = threading.current_thread().name
    sleep(delay)  # mock the wait for the IO

    logging.debug('checks & waits for the lock')

    with lock:
        logging.debug('acquired the lock')
        sleep(1)
        with open('output.dat', 'a') as fw:
            print(t_name, 'waited for the :', delay, file=fw)  # critical section
        logging.debug('releases the lock')


def main():
    """main thread"""

    list_of_threads = []
    lock_object = threading.Lock()  # sync using lock

    print(lock_object, '\n')

    for item in range(1, 6):
        time_delay = random()
        t = threading.Thread(target=worker, args=(time_delay, lock_object))
        list_of_threads.append(t)
        t.start()

    for thread in list_of_threads:
        thread.join()  # block the execution of the main thread

    print(threading.current_thread().name, 'prepares to terminate')


if __name__ == '__main__':
    main()
