# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        #We will keep an even to point at even positioned elements and odd to point at odd ones.
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = odd.next.next #Traverse odd positioned elements
            even.next = even.next.next #Traverse even positioned elements
            #Move odd and even to the next nodes
            odd = odd.next
            even=even.next
            
        odd.next = evenHead
        return head
