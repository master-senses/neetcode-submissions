class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = len(temperatures)
        answer = [0] * count
        for i in range(count - 2, -1, -1):
            j = i + 1
            while j < count and temperatures[i] >= temperatures[j]:
                if answer[j] == 0:
                    answer[i] = 0
                    break
                else:
                    j += answer[j]
            if temperatures[i] < temperatures[j]:
                answer[i] = j - i

        return answer
        