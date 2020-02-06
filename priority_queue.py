import queue

total_opened_nodes = 0

class myPriorityQueue():
    def __init__(self):
        self.queue = queue.PriorityQueue()

    # for checking if the queue is empty
    def isEmpty(self):
        return self.queue.empty()

    # for inserting an element in the queue
    def push(self, border):
        global total_opened_nodes
        self.queue.put(border)
        total_opened_nodes += 1

    # for popping an element based on Priority
    def pop(self):
        return self.queue.get()