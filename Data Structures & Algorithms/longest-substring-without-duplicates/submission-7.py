class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0
        r = 1
        best_length = 1
        sub_array = set()
        while r < len(s):
            sub_array.add(s[l])
            if s[r] not in sub_array:
                sub_array.add(s[r])
                best_length = max(best_length, len(sub_array))
            else:
                # print(s[r], sub_array)
                while s[l] != s[r]:
                    # print(sub_array, l, s[l], r, s[r])
                    # print(s[l])
                    sub_array.remove(s[l])
                    l += 1
                sub_array.remove(s[l])
                l += 1
                sub_array.add(s[r])
            r += 1
        return best_length