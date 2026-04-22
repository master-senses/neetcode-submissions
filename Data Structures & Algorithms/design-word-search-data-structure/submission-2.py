class TrieNode:

    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endofword = True

    def search(self, word: str) -> bool:
        curr = self.root
        def search_new(curr, word):
            # if len(word) == 0:
            #     return False
            for i in range(len(word)):
                if word[i] == ".":
                    # print("hi")
                    suffix = word[i+1:]
                    print(suffix, "hi")
                    # if len(suffix) == 0:
                    #     return False
                    for j in curr.children:
                        print(j)
                        if search_new(curr.children[j], suffix):
                            return True
                    return False
                elif word[i] not in curr.children:
                    # print("wassup")
                    return False
                else:
                    curr = curr.children[word[i]]
            return curr.endofword
        
        return search_new(curr, word)

        
