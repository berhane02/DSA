# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        curry = 0
        curr = result

        while l1 or l2 or curry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1+val2+curry
            curry = total//10

            curr.next = ListNode(total%10)
            curr = curr.next
 
            # move to next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next 
        return result.next