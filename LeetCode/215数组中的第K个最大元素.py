class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        heapq.heapify(heap)
        while k < len(nums):
            if nums[k] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[k])
            k += 1
        return heap[0]


import heapq

if __name__ == '__main__':
    s = Solution()
    arr = [3, 2]
    k = 2
    print(s.findKthLargest(arr, k))
