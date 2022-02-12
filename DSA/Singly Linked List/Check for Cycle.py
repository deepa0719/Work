# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Two-Pointer Method
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:                            #The try block lets us test a block of code for errors.
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            
            return True
        except:                         #The except block lets us handle the error.
            return False
