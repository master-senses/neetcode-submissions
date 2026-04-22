class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            string += str(len(strs[i])) + "#" + strs[i]
        if strs == []:
            return ":wqxary"
        return string


    def decode(self, s: str) -> List[str]:
        if s == ":wqxary":
            return []
        start = 0
        decode = []
        print(s)
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


        
        
        return lis
