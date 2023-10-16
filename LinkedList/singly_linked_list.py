# Link를 이용해서 List를 만든다.
'''
연결리스트는 인덱스가 존재하지 않고,
다음 데이터의 존재를 알려주는 다음 데이터의 주소값과 현재 데이터로 이루어져 있다.

그리고 데이터와 주소값, 두 요소로 이루어진 묶음 하나를 노드라고 부른다.

Node = [데이터][다음 주소값]

연결리스트의 특징이자 장점이라면

필요한 부분에 필요한 데이털르 원할 때 마다 삽입 삭제할 수 있다.

--> 해당 노드에 주소값이 존재한다면 다음 노드가 있다는것.
--> 해당 노드에 주소값이 없다면 해당 노드가 마지막 노드라는것.


'''

# 노드를 찍어 낼 클래스
class Node:
    def __init__(self, data, next=None):
        # Node 안에는 데이터와 주소값이 있다.
        self.data =data
        self.next =next
        
# Singly Linked List
# LinkedList 구현.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self,data):
        node = Node(data)
        if not self.head :
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    def delete(self , value):
        node = self.head
        if node.data ==value:
            self.head = node.next
            return
        
        node_exists = False
        
        while node.next:
            if node.next.data == value:
                node.next = node.next.next
                node_exists = True
                return
            node = node.next
            
        
        if not node_exists:
            print("해당 값이 없습니다!")
            return
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def display(self):
        if self.isEmpty():
            print('Node가 비어있습니다.')
        else:
            node = self.head
            while node:
                print(node.data , end = " ")
                node = node.next
            
    def search(self , value):
        if self.isEmpty():
            print('Node가 비어있습니다.')
        else:
            node = self.head
            while node != None:
                if node.data == value:
                    return True
                node = node.next
            return False
    
    def length(self):
        if self.head == None:
            return 0
        else:
            count = 0
            node = self.head
            while node != None:
                count += 1
                node = node.next
        return count
                
                 
arr = LinkedList()
arr.add(1)
arr.add(2)
arr.add(3)
arr.display()
print(arr.length())

