class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals = sorted(intervals)
        resEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= resEnd:
                resEnd = end
            else:
                print(start, resEnd)
                res += 1
                resEnd = min(end, resEnd)
            
        return res