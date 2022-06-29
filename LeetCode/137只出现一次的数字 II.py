class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_dict = {}
        for i in nums:
            if i not in temp_dict:
                temp_dict[i]=1
            else:
                temp_dict[i]+=1
                if temp_dict[i]==3:
                    temp_dict.pop(i)
        return tuple(temp_dict)[0]


if __name__ == '__main__':
    s = Solution()
    arr = [0,1,0,1,0,1,99]
    print(s.singleNumber(arr))