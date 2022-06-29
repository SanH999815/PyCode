# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first, slow = head, head
        while first and first.next:
            first = first.next.next
            slow = slow.next
            if not first:
                return False
            if first == slow:
                return True