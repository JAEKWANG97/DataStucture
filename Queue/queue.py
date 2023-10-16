# queue 구현 FIFO 방식

class Node:
    def __init__(self , data=None, next = None):
        self.data = data
        self.next = next
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def isEmpty(self):
        return self.head is None
    
    def enqueue(self,data):
        node = Node(data)
        self.count += 1
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def dequeue(self):
        node = self.head
        self.head = node.next
        self.count -= 1
        return node.data
    
    def peek(self):
        if self.isEmpty():
            return print('Queue가 비어있습니다.')
        else:
            node = self.head
            return node.data
        
    def size(self):
        return self.count
    
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.size())
print(queue.dequeue())