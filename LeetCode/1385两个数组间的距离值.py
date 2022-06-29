class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ans = 0
        for i in arr1:
            for j in arr2:
                temp = abs(i-j)
                if temp <= d:
                    break
            else:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    arr1 = [4,-3,-7,0,-10]
    arr2 = [10]
    d= 69
    print(s.findTheDistanceValue(arr1,arr2,d))