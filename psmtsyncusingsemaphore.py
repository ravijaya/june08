"""demo for the semaphore"""

import threading
from time import sleep
from random import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


class Pool:
    """semaphore pool"""

    def __init__(self):
        self.pool = []

    def add(self, t_name):
        self.pool.append(t_name)
        logging.debug(f'added to the pool: {self}')

    def remove(self, t_name):
        self.pool.remove(t_name)
        logging.debug(f'done with the pool : {self}')

    def __str__(self):
        return str(self.pool)


def worker(delay, sema, pool, lock):
    """child thread function"""
    t_id = threading.current_thread().ident
    t_name = threading.current_thread().name
    sleep(delay)  # mock the wait for the IO

    logging.debug(f'checks & waits to join the pool: {pool}')

    with sema:
        pool.add(t_name)
        sleep(1)
        with lock:
            print(f'>>{t_name}: functionality of the critical section <<')
        pool.remove(t_name)


def main():
    """main thread"""

    list_of_threads = []
    pool_object = Pool()
    lock = threading.Lock()
    sema_object = threading.Semaphore(3)  # sync using semaphore

    print(sema_object, '\n')

    for item in range(1, 5):
        time_delay = random()
        t = threading.Thread(target=worker, args=(time_delay, sema_object, pool_object, lock))
        list_of_threads.append(t)
        t.start()

    for thread in list_of_threads:
        thread.join()  # block the execution of the main thread

    print(threading.current_thread().name, 'prepares to terminate')


if __name__ == '__main__':
    main()
