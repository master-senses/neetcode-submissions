from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = {}

        wordList.append(beginWord)

        for word in wordList: # O(m^2*n)
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                if not pattern in adj:
                    adj[pattern] = []
                adj[pattern].append(word)
        
        queue = deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        count = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            count += 1
        
        return 0