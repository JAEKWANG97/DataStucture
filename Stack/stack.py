# 스택 구현!
'''
스택을 추상 자료형으로 정의해 보았을 때, 
스택(Stack)은 후입선출(LIFO)의 접근방법을 유지하는 0개 이상의 요소를 지닌 선형 리스트의 일종이라 할 수 있다.
연산	    기능
init()	    스택을 초기화
create()	스택을 생성
is_empty(s)	스택이 비어있는지 검사
is_full(s)	스택이 가득 찼는지 검사
push(e)	    스택의 맨 위에 요소 e 추가
pop(s)	    스택의 맨 위 요소를 삭제
peek(s)	    스택의 맨 위 요소를 삭제하지 않고 반환
연산	기능
init()	스택을 초기화
create()	스택을 생성
is_empty(s)	스택이 비어있는지 검사
is_full(s)	스택이 가득 찼는지 검사
push(e)	스택의 맨 위에 요소 e 추가
pop(s)	스택의 맨 위 요소를 삭제
peek(s)	스택의 맨 위 요소를 삭제하지 않고 반환
'''

class Node:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def push(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        
    def pop(self):
        if self.isEmpty():
            return print('스택이 비어있습니다.')
        else:
            node = self.head
            while node:
                if node.next == self.tail:
                    node.next = None
                    self.tail = node.next
                    return node.data
                node = node.next
    def peek(self):
        if self.isEmpty():
            return ('스택이 비어있습니다.')
        else:
            return self.tail.data
        