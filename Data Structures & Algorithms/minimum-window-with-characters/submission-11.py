import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l = 0
        r = 0
        list_t = list(t)
        substring = ""
        length = 0
        list_str = []
        str_len = math.inf
        actual = ""
        while r < len(s) and l < len(s):
            # print(l)
            while l < len(s) and s[l] not in t :
                l += 1
                r += 1
            if l >= len(s):
                break
            # print(l, r, s[l], t)
            # print(l)
            if s[l] in t:
                # print("hu")
                list_t.remove(s[l])
                substring += s[l]
                r += 1
                while len(list_t) != 0 and r < len(s):
                    substring += s[r]
                    # print(substring)
                    if s[r] in list_t:
                        length += 1
                        list_t.remove(s[r])
                    r += 1
                if len(list_t) == 0:
                    list_str.append(substring)
                    if len(substring) < str_len:
                        actual = substring
                        str_len = len(actual)
                substring = ""
                list_t = list(t)
                l += 1
                while r < len(s) and l < len(s) and s[l] not in t:
                    l += 1
                r = l
        print(list_str)      
        return actual
                    

            
            