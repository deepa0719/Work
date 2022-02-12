# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Tortoise and Hare method to find the mid of the linked list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #Now reverse the second half of the linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        #Now we have the head pointing to the first node of the first half and the prev pointing to the first node of the second half (after reversal)
        #Compare the values of the two halves
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
