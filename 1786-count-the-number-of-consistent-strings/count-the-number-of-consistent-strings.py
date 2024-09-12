class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set()
        for char in allowed:
            s.add(char)
        ans = len(words)
        for word in words:
            for char in word:
                if char not in s:
                    ans-=1
                    break
        return ans