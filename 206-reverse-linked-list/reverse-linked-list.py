# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # if not head:
        #     return None

        # newHead = head

        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        # return newHead
        prv, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
        return prv