# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):  # 哈希
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        node_dict = set()
        cur = head
        while cur:
            if cur not in node_dict:
                node_dict.add(cur)
                cur=cur.next
            else:
                return cur
        return None

    def detectCycle1(self, head):  #快慢指针
        if not head:
            return None
        first, slow = head, head
        while first:
            if first.next:
                first = first.next.next
            else:
                first = first.next
            slow = slow.next
            if first == slow:
                break
        if not first:
            return None
        first = head
        while first!=slow:
            first=first.next
            slow=slow.next
        return first
