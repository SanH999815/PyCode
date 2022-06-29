class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_tab = {}
        for i in nums:
            if i in hash_tab:
                return True
            else:
                hash_tab[i]=1
        return False