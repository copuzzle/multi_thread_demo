#-*- encoding: utf-8 -*-
import thread
import time
import sys


def print_time(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (thread_name, time.ctime(time.time()))
        sys.stdout.flush()


try:
    thread.start_new_thread(print_time, ("Thread-1", 2))
    thread.start_new_thread(print_time, ("Thread-2", 2))
except:
    print "Error: unable to start thread"

while 1:
    pass