class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        
        for p in range(len(nums1) - 1, 0, -1):
            if m <= 0 or n <= 0:
                break
            if nums1[m - 1] > nums2[n - 1]:
                nums1[p] = nums1[m - 1]
                m -= 1
                # print(nums1[p])
            else:
                nums1[p] = nums2[n - 1]
                n -= 1
            print(nums1)
        
        while n > 0:
            # print(n)
            nums1[n - 1] = nums2[n - 1]
            print("n loop", nums1)
            n -= 1
        