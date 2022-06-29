class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        l = 1
        r = num>>1
        while l <= r:
            mid = l + ((r-l)>>1)
            if mid**2 == num:
                return True
            elif mid**2 < num:
                l = mid +1
            else:
                r = mid -1
        return False

if __name__ == '__main__':
    s = Solution()
    num = 14
    print(s.isPerfectSquare(num))
