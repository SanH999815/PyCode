class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res

if __name__ == '__main__':
    s = Solution()
    arr = [4,1,2,1,2]
    print(s.singleNumber(arr))