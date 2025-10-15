# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumy =  ListNode(-1)
        dumy.next = head

        first, second = dumy, dumy
        for i in range(n):
            second = second.next
        while second.next != None:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return dumy.next

        