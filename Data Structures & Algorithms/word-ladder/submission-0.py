class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        
        print(adj)

        visited = set(beginWord)
        queue = deque()
        queue.append(beginWord)
        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            res += 1
        return 0


        