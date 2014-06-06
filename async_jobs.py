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
        try:
            task = _task_queue.get()
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
                _task_queue.task_done()
                print len(_task_queue.queue)
                time.sleep(0.5)
        except Exception as ex:
            logging.warning(ex)



def handle_result(result):
    print(type(result), result)

if __name__ == '__main__':
    t = threading.Thread(target=_task_queue_consumer)
    #t.daemon = True
    t.start()

    #async_call(func_a, handle_result, 1, 2)
    #async_call(func_b, handle_result)
    #async_call(func_c, handle_result, 1, 2, 3)
    #async_call(func_c, handle_result, 1, 2, 3, 4)
    funcs = [func_a, func_b, func_c]
    while 1:
        f = random.choice(funcs)
        async_call(f, handle_result, 1, 2, 3, )
        time.sleep(0.3)

    _task_queue.join()