from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return [[""]]

        final_dict = {}
        # strs_dict = {}
        
        for i in strs:
            count = Counter(i)
            new_count = sorted(count)
            new_count2 = []
            for j in new_count:
                new_count2.append(j)
                new_count2.append(count[j])
            new_count2 = tuple(new_count2)
            # print(i, count)
            if new_count2 in final_dict:
                final_dict[new_count2].append(i)
            else:
                final_dict[new_count2] = [i]
        res = []
        for i in final_dict.values():
            res.append(i)
        print(res)
        return res
