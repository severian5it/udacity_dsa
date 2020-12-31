class PriorityQueue(object):
    def __init__(self):
        self.q = []

    def __repr__(self):
        sorted_list = sorted(self.q, reverse=True)
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in sorted_list])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    # for inserting an element in the queue
    def push(self, data):
        self.q.append(data)

        # for popping an element based on Priority

    def pop(self):
        if len(self.q)> 0:
            max = 0
            for i in range(len(self.q)):
                if self.q[i] < self.q[max]:
                    max = i
            item = self.q[max]
            del self.q[max]
            return item
        else:
            return -1

myQueue = PriorityQueue()
myQueue.push(12)
myQueue.push(1)
myQueue.push(14)
myQueue.push(7)
print(myQueue)
while not myQueue.isEmpty():
    print(myQueue.pop())