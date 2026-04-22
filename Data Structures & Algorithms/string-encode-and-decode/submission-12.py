class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode += str(len(i)) + "," + i
        return encode
            
        

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decode = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ",":
                j += 1
            count = int(s[i:j])
            j += 1
            decode.append(s[j: j + count])
            i = j + count

        return decode


