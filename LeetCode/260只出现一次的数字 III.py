class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in nums:
            temp ^= i
        temp = temp&(-temp)
        res1 = 0
        res2 = 0
        for i in nums:
            if temp&i == 0:
                res1 ^= i
            else:
                res2 ^= i
        return [res1, res2]

if __name__ == '__main__':
    s = Solution()
    arr = [0,1]
    print(s.singleNumber(arr))
