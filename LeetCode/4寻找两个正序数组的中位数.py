class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        if (l1+l2)%2!=0:
            k = (l1+l2)//2 + 1
            res = self.fun(nums1,l1,nums2,l2,k)
            return res
        else:
            k = (l1+l2)//2
            res = (self.fun(nums1,l1,nums2,l2,k)+self.fun(nums1,l1,nums2,l2,k+1))/2
            return res

    def fun(self, arr1, l1, arr2, l2, k):
        if l1 > l2:
            return self.fun(arr2, l2, arr1, l1, k)
        if l1 == 0:
            return arr2[k - 1]
        if k == 1:
            return min(arr1[0], arr2[0])

        k1 = min(l1, k // 2)
        k2 = k - k1
        if arr1[k1 - 1] == arr2[k2 - 1]:
            return arr1[k1 - 1]
        elif arr1[k1 - 1] < arr2[k2 - 1]:
            return self.fun(arr1[k1:], len(arr1[k1:]), arr2, len(arr2), k2)
        else:
            return self.fun(arr1, len(arr1), arr2[k2:], len(arr2[k2:]), k1)


if __name__ == '__main__':
    arr1 = [1,2,3]
    arr2 = [4,4,4]
    s = Solution()
    print(s.findMedianSortedArrays(arr1,arr2))
