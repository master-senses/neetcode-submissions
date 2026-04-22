class Solution:
    def encode(self, strs: List[str]) -> str:
        # encode = ""
        # for i in strs:
        #     encode += str(len(i)) + "," + i
        # return encode
        return_string = ""
        for i in strs:
            count = len(i)
            return_string += str(count) + ","+ i
        print(return_string)
        return return_string
            
    def decode(self, s: str) -> List[str]:
        # if s == "":
        #     return []
        # decode = []
        # i = 0
        # while i < len(s):
        #     j = i
        #     while s[j] != ",":
        #         j += 1
        #     count = int(s[i:j])
        #     j += 1
        #     decode.append(s[j: j + count])
        #     i = j + count

        # return decode
        if str == "":
            return []
        
        i = 0
        final_list = []
        while i < len(s):
            j = i
            while s[j] != ",":
                j += 1
            skip = int(s[i:j])
            print(skip)
            j += 1
            word = s[j: skip + j]
            print(word)
            i = skip + j
            final_list.append(word)

        return final_list


