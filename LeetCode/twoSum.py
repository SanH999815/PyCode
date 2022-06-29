class Solution:
    def twoSum(self, nums, target):
        hash_table = dict()
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            hash_table[nums[i]] = i


if __name__ == '__main__':
    S = Solution()
    print(S.twoSum([3, 2, 4], 6))
