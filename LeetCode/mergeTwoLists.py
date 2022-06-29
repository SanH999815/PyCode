# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + str(self.next)


def Print_listNode(l1):
    p = l1
    while p:
        print(p.val, end='-')
        p = p.next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists1(self, list1: ListNode, list2: ListNode):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head = ListNode(-1)
        pre = head
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
                pre = pre.next
            else:
                pre.next = list2
                list2 = list2.next
                pre = pre.next
        if list1:
            pre.next = list1
        else:
            pre.next = list2
        return head.next
        pass


if __name__ == '__main__':
    s = Solution()
    list1 = []
    for i in [1, 2, 4]:
        node = ListNode(i)
        list1.append(node)
    for i in range(len(list1) - 1):
        if i != len(list1) - 1:
            list1[i].next = list1[i + 1]
    list2 = []
    for i in [1, 3, 4]:
        node = ListNode(i)
        list2.append(node)
    for i in range(len(list2) - 1):
        if i != len(list1) - 1:
            list2[i].next = list2[i + 1]
    Print_listNode(s.mergeTwoLists1(list1[0], list2[0]))
