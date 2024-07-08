class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        orig = []
        for i in range(1, n + 1):
            orig.append(i)
        start = 0
        while len(orig) > 1:
            # print("removing ", orig[(start + k%n - 1)%n])
            del orig[(start + k % n -1)%n]
            start = (start +k % n -1)%n
            # print("New start", start, orig[start])
            n -= 1
        return orig[0]