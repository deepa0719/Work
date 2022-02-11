'''A simple solution to delete the nodes having value T is to traverse over the linked list and just remove the next pointers to the node having value as T. Now, usually in deletion problem of linked list, there can be multiple cases where node to be deleted is either a head node or other node in rest of list. We usually make use of a dummy node at the start or sentinel node to avoid handling multiple edge cases and write a clean uniform solution.

So, the algorithm we are using can be summarised as -

1. Initialize a dummy/sentinel node having its next pointer pointing to the head of linked list and another node pointer prev pointing to this dummy node.
2. Start iterating over head of linked list
3. If current node's value is not equal to T, we can just move to next node without deleting current node. In this case,
4. We first update prev pointer and point it to current head
5. Then move head to next node.
6. Otherwise, if head -> val == T, we know that this node needs to be deleted. In this case,
7. We can just update the next pointer of previous node to the next pointer of current node. This will basically remove the current node from list.
8. Then, we update head to its next node just as in previous case.
9. Finally, ignore the dummy node created at start and return its next node.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], value: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        while head:
            if head.val != value:
                prev = head
            else:
                prev.next = head.next
            head = head.next
        return dummy.next
        
        
