# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):  # 哈希
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        cur = headA
        node_dict = set()
        while cur:
            node_dict.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in node_dict:
                return cur
            else:
                cur = cur.next
        return None

    def getIntersectionNode1(self, headA, headB):  # 有限指针
        if not headA or not headB:
            return None
        lA, lB = 0, 0
        cur = headA
        pre_A = None
        while cur:
            lA += 1
            pre_A = cur
            cur = cur.next
        cur = headB
        pre_B = None
        while cur:
            lB += 1
            pre_B = cur
            cur = cur.next
        if pre_A != pre_B:
            return None
        n = lA - lB
        cur_1 = headA if n > 0 else headB
        cur_2 = headB if cur_1 == headA else headA
        n = abs(n)
        while n != 0:
            n -= 1
            cur_1 = cur_1.next
        while True:
            if cur_1 == cur_2:
                return cur_1
            cur_1 = cur_1.next
            cur_2 = cur_2.next

    def getIntersectionNode2(self, headA, headB):  # 有限指针 优化一下
        if not headA or not headB:
            return None
        n = 1
        cur_A = headA
        while cur_A.next:
            n += 1
            cur_A = cur_A.next
        cur_B = headB
        n -= 1
        while cur_B.next:
            n -= 1
            cur_B = cur_B.next
        if cur_B != cur_A:
            return None
        cur_A = headA if n > 0 else headB
        cur_B = headB if cur_A == headA else headA
        n = abs(n)
        while n != 0:
            n -= 1
            cur_A = cur_A.next
        while True:
            if cur_A == cur_B:
                return cur_B
            cur_A = cur_A.next
            cur_B = cur_B.next

    def getIntersectionNode3(self, headA, headB):  # 有限指针 优化一下
        if not headA or not headB:
            return None
        node_A, node_B = headA, headB
        while node_A != node_B:
            node_A = node_A.next if node_A is not None else headB
            node_B = node_B.next if node_B is not None else headA
        return node_A


if __name__ == '__main__':
    s = Solution()
    arr = [4, 1, 8, 4, 5]
    arr_node = []
    for i in arr:
        new_node = ListNode(i)
        arr_node.append(new_node)
    for i in range(len(arr_node) - 1):
        arr_node[i].next = arr_node[i + 1]
    arr_node[len(arr_node) - 1].next = None
    arr2 = [5, 6, 1]
    arr_node2 = []
    for i in arr2:
        new_node = ListNode(i)
        arr_node2.append(new_node)
    for i in range(len(arr_node2) - 1):
        arr_node2[i].next = arr_node2[i + 1]
    arr_node2[len(arr_node2) - 1].next = arr_node[2]
    print(s.getIntersectionNode3(arr_node[0], arr_node2[0]))
