class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid +1
            else:
                return mid
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.search([],-1))
