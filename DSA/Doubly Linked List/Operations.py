'''
Adding a node to DLL:
If we want to insert a new node cur after an existing node prev, we can divide this process into two steps:
1. link cur with prev and next, where next is the original next node of prev;
2. re-link the prev and next with cur. 

Deleting a node in DLL:
If we want to delete an existing node cur from the doubly linked list, we can simply link its previous node prev with its next node next.
'''

class Node:
    
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode
    
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size=0
        

    def get(self, index: int) -> int:
        if index>=self.size:
            return -1
        
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return  
        
        prev = self.head
        for i in range(index):
            prev = prev.next
        
        #Adding node between prev and prev.next
        cur = Node(val, prev.next)
        prev.next = cur
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size:
            return 
        
        prev = self.head
        for i in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size-=1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
