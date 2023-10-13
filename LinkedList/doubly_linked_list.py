class Node:
    def __init__(self , data , next = None , previous = None):
        self.data = data
        self.next = next
        self.previous = previous
        
class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self , data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
    
    def pop(self,index=None):
        if not self.head:
            return print('리스트가 비어 있습니다.')
        if index is None:
            if self.head ==self.tail: # 단말노드일 때
                self.head = self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
            return
        
        #특정 인덱스 노드 삭제
        node=  self.head
        count = 0
        while node:
            if count == index:
                if node.previous: #삭제노드가 head가 아닌경우
                    node.previous.next = node.next
                else: #삭제노드가 head 인 경우
                    self.head = node.next
                    node.next.previous = None
                    
                if node.next: #삭제노드가 tail이 아닌 경우
                    node.next.previous = node.previous
                else:
                    self.tail = node.previous
                    node.previous.next = None
                return 
            count += 1
            node = node.next
      
    def isEmpty(self):
        if self.head:
            return False
        else:
            return True
                         
    def search(self , value):
        if self.isEmpty():
            print('리스트가 비어있습니다.')
        else:
            node = self.head
            while node:
                if node.data == value:
                   return True
                node = node.next
            return False
        
    def length(self):
        if self.isEmpty():
            return 0
        else:
            count = 0
            node = self.head
            while node:
                count += 1
                node =node.next        
            return count
        
    def display(self):
        if self.isEmpty():
            return print('리스트가 비어있습니다.')
        else:
            node = self.head
            while node:
                print(node.data , end = ' ')
                node = node.next
            print()
            return
        
        
arr = Doubly_linked_list()

arr.add(1)
arr.add(2)
arr.add(3)
arr.display()
arr.pop()
arr.display()
arr.search(1)
arr.add(3)
arr.length()
arr.isEmpty()
arr.pop(0)
arr.display()