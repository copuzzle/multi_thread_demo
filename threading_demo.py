#-*- encoding: utf-8 -*-
import threading
import time
import sys
exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, delay):
        super(MyThread, self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.delay, 3)
        print "Exiting " + self.name


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        counter -= 1
        print "%s: %s" % (thread_name, time.ctime(time.time()))
        sys.stdout.flush()

thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
thread3 = MyThread(3, "Thread-3", 2)

thread1.start()
thread2.start()
thread3.start()

print "------Exiting Main Thread------"
