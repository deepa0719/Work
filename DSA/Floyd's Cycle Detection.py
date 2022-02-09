# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''One way to do this would be as follows:
        slow = fast = ans = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow !=ans:
                    slow=slow.next
                    ans = ans.next
                return ans
        return None
        '''
        
        #Second Method
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
