# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        ptr1 = ptr2 = head
        length = 1
        
        while ptr1.next:
            ptr1=ptr1.next
            length+=1
            
        k = k%length
        if k == 0:
            return head
        
        #Make the linked list circular. i.e. the last node is now pointing to the first node
        ptr1.next = head
        
        #Now traverse to the (length-k)th node
        for _ in range(length-k-1):
            ptr2 = ptr2.next
        
        #Now cut the list from this node
        ans = ptr2.next
        ptr2.next = None
        return ans
