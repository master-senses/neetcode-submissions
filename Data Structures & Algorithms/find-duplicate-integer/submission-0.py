class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force, takes O(n) time and O(n) space
        # add every element to a set and check when collision happens
        # binary search, but that needs array to be sorted. Sorting takes O(nlogn)
        # if we sort, we can use O(1) space by just checking if the next element is equal
        # to the element we have rn

        visited = set()

        for i in nums:
            if i in visited:
                return i
            visited.add(i)

        return -1