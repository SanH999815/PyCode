# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):  # 前插法
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        new_head = ListNode(0)
        cur = head
        while cur and cur.next:
            p = cur.next
            cur.next = new_head.next
            new_head.next = cur
            cur = p
        cur.next = new_head.next
        new_head.next = cur
        return new_head.next

    def reverseList2(self, head):  # 改变链表方向
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        cur = head.next
        pre = head
        head.next = None
        while cur:
            n1 = cur.next
            cur.next = pre
            pre = cur
            cur = n1
        return cur

