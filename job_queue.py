#-*- encoding: utf-8 -*-
import Queue
import threading
import time
import random
runFlag = 1


class JobThread(threading.Thread):
    def __init__(self, thread_name, num):
        super(JobThread, self).__init__()
        self.name = thread_name
        self.num = num

    def do_job(self):
        print "Starting " + self.name
        job(self.num)
        print "Exiting " + self.name + "; "


def job(num):
    r_t = random.randrange(1, 3)
    time.sleep(r_t)
    print num*"*"

job_queue = Queue.Queue(5)
threads = []
count = 0
while 1:
    r_t = random.randrange(10, 30)
    thr = JobThread("Thread-%s" % count, r_t)
    job_queue.put(thr)