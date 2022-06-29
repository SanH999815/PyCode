# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        oH, oT, eH, eT = head, head, head.next, head.next
        cur = head.next.next
        flag = True
        while cur:
            next_node = cur.next
            if flag:
                oT.next = cur
                oT = cur
                flag = False
            else:
                eT.next = cur
                eT = cur
                flag = True
            cur = next_node
        oT.next = eH
        eT.next = None
        return oH


if __name__ == '__main__':
    s = Solution()
    arr = [1,2,3,4,5]
    arr_node = []
    for i in arr:
        new_node = ListNode(i)
        arr_node.append(new_node)
    for i in range(len(arr_node) - 1):
        arr_node[i].next = arr_node[i + 1]
    arr_node[len(arr_node) - 1].next = None
    print(s.oddEvenList(arr_node[0]))
