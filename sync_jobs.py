#-*- encoding: utf-8 -*-
import logging
import Queue
import threading
import time
import random

def func_a(a, b):
    return a + b


def func_b():
    pass


def func_c(a, b, c):
    return a, b, c

# 异步任务队列
_task_queue = Queue.Queue(3)


def async_call(function, callback, *args, **kwargs):
    _task_queue.put({
        'function': function,
        'callback': callback,
        'args': args,
        'kwargs': kwargs
    })


def _task_queue_consumer():
    """
    异步任务队列消费者
    """
    while True:
        if _task_queue.full():
            q_len = _task_queue.qsize()
            print q_len
            #t_lock.acquire()
            #_task_queue.mutex.acquire()
            #_task_queue.join()
            while q_len:
                try:
                    task = _task_queue.get()
                    _task_queue.mutex.acquire()
                    function = task.get('function')
                    callback = task.get('callback')
                    args = task.get('args')
                    kwargs = task.get('kwargs')
                    try:
                        if callback:
                            callback(function(*args, **kwargs))
                    except Exception as ex:
                        if callback:
                            callback(ex)
                    finally:

                        #_task_queue.task_done()
                        print _task_queue.qsize()
                        time.sleep(0.3)

                except Exception as ex:
                    logging.warning(ex)
                q_len -= 1
            #_task_queue.mutex.release()
            #t_lock.release()
            print 200 * "-"
        else:
            time.sleep(0.1)


t_lock = threading.Lock()


def handle_result(result):
    print(type(result), result)

if __name__ == '__main__':
    t = threading.Thread(target=_task_queue_consumer)
    #t.daemon = True
    t.start()

    funcs = [func_a, func_b, func_c]
    while 1:
        f = random.choice(funcs)
        async_call(f, handle_result, 1, 2, 3, )
        time.sleep(0.1)

    #_task_queue.join()