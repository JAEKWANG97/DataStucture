class Node():
    def __init__(self , data , next = None , previous = None):
        self.data = data
        self.next = next
        self.previous = previous
class circular_linked_list():
    def __init__(self):
        self.head = None
        self.tail= None
        
    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head= node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.tail.next = self.head
        
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def pop(self, value):
        if self.isEmpty():
            return print('리스트가 비어 있습니다.')
        else:
            node = self.head
            if node.data == value:
                self.head = node.next
                self.tail.next = self.head
                self.head.previous = self.tail
                return 
            while node:
                if node.data == value:
                    if node == self.tail:
                        self.tail = node.previous
                    node.previous.next = node.next
                    node.next.previous = node.previous
                    return
                if node == self.tail:
                    break
                node = node.next
            return print('해당 값이 없습니다.')
        
    def display(self):
        if self.isEmpty():
            print('')
        else:
            node =self.head
            while node:
                print(node.data , end = ' ')
                if node == self.tail:
                    break
                node = node.next
            print()
            
    def search(self,value):
        if self.isEmpty():
            return print('리스트가 비어 있음')
        node = self.head
        while node:
            if node.data == value:
                return True
            elif node == self.tail:
                return False
            node = node.next
        return False
    
    def length(self):
        if self.isEmpty(): return print(0)
        node = self.head
        count = 0
        while node:
            count += 1
            if node == self.tail:
                return count
            node = node.next
        return count
        
arr = circular_linked_list()
arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)
arr.display()
arr.pop(1)
arr.display()
arr.pop(4)
arr.display()

print(arr.search(5))

print(arr.length())