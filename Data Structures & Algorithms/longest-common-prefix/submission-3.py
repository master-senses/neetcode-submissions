class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        word = strs[0]
        pref = word
        for i in strs:
            mini = min(len(pref), len(i))
            j = 0
            while j < mini:
                if pref[j] == i[j]:
                    j += 1
                else:
                    break
            pref = pref[:j]

        return pref
                


