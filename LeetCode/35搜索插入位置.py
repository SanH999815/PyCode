class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,6]
    print(s.searchInsert(nums,7))