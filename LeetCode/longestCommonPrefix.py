class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs[0])
        temp = ''
        ans = ''
        for i in range(n):
            temp = strs[0][:i+1]
            for j in range(1, len(strs)):
                if strs[j][:i+1] != temp:
                    break
            else:
                ans = temp
                continue
            break
        return ans




if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
