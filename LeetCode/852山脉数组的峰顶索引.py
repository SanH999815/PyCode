class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, len(arr)-1
        while l<r:
            mid = l + ((r - l) >> 1)
            if arr[mid]<arr[mid+1]:
                l=mid+1
            elif arr[mid]<arr[mid-1]:
                r = mid-1
            else:
                return mid



if __name__ == '__main__':
    s = Solution()
    arr = [0,2,1,0]
    print(s.peakIndexInMountainArray(arr))