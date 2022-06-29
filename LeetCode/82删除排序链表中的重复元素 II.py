# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates_vertion_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        while head and head.next and head.val == head.next.val:

            cur = head.next
            while cur and cur.val == head.val:
                cur = cur.next
            head = cur
        if head:
            cur = head
            pre = None
            while cur and cur.next:
                if cur.val == cur.next.val:
                    cut_star = cur
                    node_temp = cur.next
                    while node_temp and node_temp.val == cut_star.val:
                        cut_end = node_temp
                        node_temp = node_temp.next
                    pre.next = cut_end.next
                    cur = pre
                else:
                    pre = cur
                    cur = cur.next
        return head

    def vertion_02(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp_head = ListNode(-101,head)
        cur = head
        pre = temp_head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cut_star = cur
                node_temp = cur.next
                while node_temp and node_temp.val == cut_star.val:
                    cut_end = node_temp
                    node_temp = node_temp.next
                pre.next = cut_end.next
                cur = pre
            else:
                pre = cur
                cur = cur.next
        return temp_head.next

if __name__ == '__main__':
    s = Solution()
    arr = [1, 1, 1, 2 ,2]
    arr_node = []
    for i in arr:
        new_node = ListNode(i)
        arr_node.append(new_node)
    for i in range(len(arr_node) - 1):
        arr_node[i].next = arr_node[i + 1]
    arr_node[len(arr_node) - 1].next = None
    print(s.deleteDuplicates(arr_node[0]))
