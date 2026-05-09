from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return [[""]]

        final_dict = {}
        # strs_dict = {}
        
        for i in strs:
            # count = Counter(i)
            new_str = sorted(i)
            new_str = tuple(new_str)
            if new_str in final_dict:
                final_dict[new_str].append(i)
            else:
                final_dict[new_str] = [i]
        res = []
        for i in final_dict.values():
            res.append(i)
        print(res)
        return res
