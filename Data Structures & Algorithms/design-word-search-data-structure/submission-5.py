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
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for j in cur.children:
                        if dfs(i + 1, cur.children[j]):
                            return True
                    return False
                elif c not in cur.children:
                    return False
                else:
                    cur = cur.children[c]
            
            return cur.endofword
        
        return dfs(0, self.root)

        
