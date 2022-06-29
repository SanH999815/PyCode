class Solution(object):
    def removeDuplicates1(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        count = 0
        while i < n - 1:
            if nums[count] == nums[count + 1]:
                nums.remove(nums[count])
            else:
                count += 1
            i += 1
        return len(nums)

    def removeDuplicates(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        fast, show = 1, 1
        temp = nums[0]
        while fast<n:
            if nums[fast] == temp:
                fast+=1
            else:
                nums[show] = nums[fast]
                temp = nums[show]
                fast, show = fast+1, show+1
        return show




if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    print(s.removeDuplicates(arr))
    print(arr)
