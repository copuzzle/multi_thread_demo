#-*- encoding: utf-8 -*-
import Queue,threading,time,random


class consumer(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.daemon = False
        self.queue = que

    def run(self):
        while True:
            item = self.queue.get()
            if item == None:
                break
            print self.name, item
            self.queue.task_done()
        self.queue.task_done()
        return
que = Queue.Queue()

consumers = [consumer(que) for x in range(3)]
for c in consumers:
    c.start()
for x in range(10):
    item = random.random()
    time.sleep(item)
    que.put(item, True, None)


que.put(None)
que.put(None)
que.put(None)
que.join()
