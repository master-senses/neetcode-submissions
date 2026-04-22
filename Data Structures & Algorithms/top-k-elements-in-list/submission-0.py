from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        count = count.most_common()
        # print(count)
        freq = []
        for i in range(k):
            freq.append(count[i][0])
        # freq = []
        # j = 0
        # return list(count.keys())
        return freq




        