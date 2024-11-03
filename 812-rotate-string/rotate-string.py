class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for idx in range(len(s)):
            if s[idx:] + s[:idx] == goal:
                return True
        
        return False