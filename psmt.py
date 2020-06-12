"""demo for the multi-threading / boiler plate"""

import threading
from time import sleep
from random import random
from pprint import pprint as pp


def worker(delay):
    """thread function"""
    t_id = threading.current_thread().ident
    t_name = threading.current_thread().name
    # sleep(delay)  # mock the wait for the IO
    print(t_name, 'waited for the :', delay)   # critical section


def main():
    """main thread"""

    list_of_threads = []

    for item in range(1, 6):
        time_delay = random()
        t = threading.Thread(target=worker, args=(time_delay,), name=f't{item}')
        list_of_threads.append(t)
        t.start()

    for thread in list_of_threads:
        thread.join()  # block the execution of the main thread

    print(threading.current_thread().name, 'prepares to terminate')
    pp(list_of_threads)


if __name__ == '__main__':
    main()
