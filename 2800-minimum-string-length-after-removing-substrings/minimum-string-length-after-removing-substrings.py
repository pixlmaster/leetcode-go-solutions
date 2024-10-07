class Solution:
    def minLength(self, s: str) -> int:
        deleted = 0
        n = len(s)
        while True:
            for i in range(n-1):
                if s[i:i+2] == "AB" or s[i:i+2] == "CD":
                    s = s[:i] + s[i+2:]
                    deleted += 2
            if deleted == 0:
                return len(s)
            deleted = 0
            