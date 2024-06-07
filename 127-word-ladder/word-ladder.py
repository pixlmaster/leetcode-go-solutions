class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        q = deque()
        q.append((beginWord,0))
        ans = 0
        visited = set()
        visited.add(beginWord)

        while q:
            # print(q)
            curr, dist = q.popleft()
            if curr == endWord:
                return dist+1
            # TODO edge case of starting word
            for word in wordList:
                if word not in visited and self.edits(curr,word, n)==1:
                    visited.add(word)
                    q.append((word,dist+1))
                    
    
        return 0


    def edits(self, s1: str, s2: str, n: int) ->  int:
        edit = 0
        for i in range(n):
            if s1[i]!=s2[i]:
                edit+=1
        
        return edit