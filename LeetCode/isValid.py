# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 单个字符 ][这样乱搞的
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = ['(', '{', '[']
        stack = []
        count_stack = 0
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i not in arr and count_stack == 0:
                return False
            if i in arr:
                stack.append(i)
                count_stack += 1
            else:
                if ((i == ')' and stack[count_stack - 1] == arr[0]) or
                        (i == '}' and stack[count_stack - 1] == arr[1]) or
                        (i == ']' and stack[count_stack - 1] == arr[2])):
                    stack.pop()
                    count_stack -= 1
                else:
                    return False
        if len(stack) != 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(){}}{"))
