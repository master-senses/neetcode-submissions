class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([timestamp, value])
        else:
            self.store[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        # Could do O(logn) if values are sorted
        if key not in self.store or timestamp < self.store[key][0][0]:
            return ""
        # self.store[key].sort() # O(nlogn)
        # if timestamp < self.store[key][0]
        start = 0
        end = len(self.store[key]) - 1
        print(self.store[key])
        i = 0
        while start <= end:
            mid = (end + start) // 2
            if self.store[key][mid][0] == timestamp:
                return self.store[key][mid][1]
            elif self.store[key][mid][0] < timestamp:
                start = mid + 1
                i = mid
            else:
                end = mid - 1
        # if i == 0:
        #     return ""
        return self.store[key][i][1]
        

        
