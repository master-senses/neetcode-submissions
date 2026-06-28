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
        if key not in self.store:
            return ""
        # self.store[key].sort() # O(nlogn)
        val = 0
        i = 0
        while i < len(self.store[key]) and self.store[key][i][0] <= timestamp: # O(n)
            i += 1
        if i == 0:
            return ""
        return self.store[key][i - 1][1]
        

        
