# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):  # O(1)方法
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        cur = head
        while cur:
            copy_node = cur.next
            copy_node.random = cur.random.next if cur.random else None
            cur = copy_node.next
        new_head = head.next
        cur = head
        while cur and cur.next.next is not None:
            copy_node = cur.next
            cur.next = cur.next.next
            copy_node.next = copy_node.next.next
            cur = cur.next
        copy_node = cur.next
        cur.next = None
        copy_node.next = None
        return new_head
