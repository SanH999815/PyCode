class Solution(object):
    def mergeSort(self, arr, temp, low, high):
        if low == high:
            return 0
        mid = low + ((high - low) >> 1)
        return self.mergeSort(arr, temp, low, mid) + self.mergeSort(arr, temp, mid + 1, high) + self.merge(arr, temp, low, mid, high)

    def merge(self, arr, temp, low, mid, high):
        i, j, k, ans = low, mid + 1, low, 0
        while i <= mid and j <= high:
            if arr[i] > arr[j]:
                ans += high - j + 1
                temp[k] = arr[i]
                k += 1
                i += 1
            else:
                temp[k] = arr[j]
                k += 1
                j += 1
        while i <= mid:
            temp[k] = arr[i]
            k += 1
            i += 1
        while j <= high:
            temp[k] = arr[j]
            k += 1
            j += 1
        arr[low:high + 1] = temp[low:high + 1]
        return ans

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        temp = [0] * n
        return self.mergeSort(nums, temp, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    arr = [7, 5, 6, 4]
    print(s.reversePairs(arr))
