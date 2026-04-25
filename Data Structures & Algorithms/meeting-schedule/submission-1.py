"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
        interv = []
        for i in range(len(intervals)):
            interv.append([intervals[i].start, intervals[i].end])
        
        interv = sorted(interv)
        print(interv)
        end = interv[0][1]
        for i in range(1, len(interv)):
            print(interv[i][0], end)
            if interv[i][0] < end:
                return False
            end = interv[i][1]

        # for i in range(len(intervals)):
        return True
