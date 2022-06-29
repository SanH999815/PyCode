# 爬楼梯
import time


class Solution(object):
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        else:
            a, b= 1, 2
            for i in range(3,n+1):
                temp = b
                b = a+b
                a = temp
        return b

    mem = [0]*46
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if Solution.mem[n]>0:
            return Solution.mem[n]
        if n == 1 or n == 2:
            Solution.mem[n]=n
            return n
        Solution.mem[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return Solution.mem[n]



if __name__ == '__main__':
    s = Solution()
    star_time = time.time()
    print(s.climbStairs(44))
    end_time = time.time()
    print(end_time-star_time)