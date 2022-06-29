# 移除元素
class Solution(object):
    def removeElement1(self, nums: list, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        fast, show = 0, 0
        while fast<n:
            if nums[fast] != val:
                nums[show] = nums[fast]
                show += 1
            fast+=1
        return show

    def removeElement(self, nums: list, val):
        n = nums.count(val)
        for i in range(n):
            nums.remove(val)
        return len(nums)





if __name__ == '__main__':
    s = Solution()
    arr = [0,1,2,2,3,0,4,2]
    print(s.removeElement(arr, 2))
    print(arr)
