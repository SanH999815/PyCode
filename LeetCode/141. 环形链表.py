# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head): # 快慢指针
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

    def hasCycle1(self, head): # 哈希
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        node_dict = set()
        cur = head
        while cur:
            if cur not in node_dict:
                node_dict.add(cur)
                cur = cur.next
            else:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    arr = [3,2,0,-4]
    arr_node = []
    for i in arr:
        new_node = ListNode(i)
        arr_node.append(new_node)
    for i in range(len(arr_node)-1):
        arr_node[i].next = arr_node[i+1]
    arr_node[len(arr_node)-1].next=arr_node[1]
    print(s.hasCycle1(arr_node[0]))