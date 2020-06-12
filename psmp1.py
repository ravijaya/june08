"""multiprocessing"""

import multiprocessing


def task_set(lock):
    """child process function"""
    p_name = multiprocessing.current_process().name
    p_id = multiprocessing.current_process().pid

    with lock:
        print(p_name, ':', p_id)  # CS


def main():
    """parent process"""
    parent = multiprocessing.current_process()
    print(parent.name, ':', parent.pid)
    lock = multiprocessing.Lock()

    for item in range(1, 6):
        p = multiprocessing.Process(target=task_set, args=(lock,))
        p.start()

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
