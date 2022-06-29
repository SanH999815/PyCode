# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.arr = []

    def add(self, value):
        self.arr.append(value)

    def pop(self):
        t = self.arr.pop()
        return t


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        return temp == temp[::-1]

    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return head
        fast, slow, pre = head, head, None
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        n1 = slow.next
        while n1:
            n2 = n1.next
            n1.next = pre
            pre = n1
            n1 = n2
        res = True
        n1 = head
        n2 = pre
        while res and n2:
            if n1.val != n2.val:
                res = False
            n1 = n1.next
            n2 = n2.next
        n2 = pre
        pre = None
        while n2:
            n1 = n2.next
            n2.next = pre
            pre = n2
            n2 = n1
        return res

if __name__ == '__main__':
    s = Solution()
    arr = [1,2,2,1]
    arr_node = []
    for i in arr:
        new_node = ListNode(i)
        arr_node.append(new_node)
    for i in range(len(arr_node)-1):
        arr_node[i].next = arr_node[i+1]
    arr_node[len(arr_node)-1].next=None
    print(s.isPalindrome2(arr_node[0]))
