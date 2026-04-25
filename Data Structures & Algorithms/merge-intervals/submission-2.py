class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        
        for start, end in intervals:
            if not res or res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1] = [res[-1][0], max(res[-1][1], end)]
        
        return res


            

            

