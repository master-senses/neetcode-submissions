class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        inter_dict = {}
        res = []
        intervals = sorted(intervals)
        for i in intervals:
            inter_dict[tuple(i)] = False

        for i in range(len(intervals)):
            print(intervals[i], inter_dict[tuple(intervals[i])])
            if not inter_dict[tuple(intervals[i])]:
                maxi = intervals[i]
                inter_dict[tuple(intervals[i])] = True
                for j in range(i + 1, len(intervals)):
                    if not inter_dict[tuple(intervals[j])]:
                        if maxi[0] <= intervals[j][1] and maxi[1] >= intervals[j][0]:
                            maxi = [min(maxi[0], intervals[j][0]), max(maxi[1], intervals[j][1])]
                            inter_dict[tuple(intervals[j])] = True
                res.append(maxi)
        
        return res


            

            

