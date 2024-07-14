class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        """
        Binary search on the solution with min dist x
        if you can place it, try between x and max
        if you cannot, search between this and last tried
        """
        position.sort()
        n = len(position)
        if n == 2:
            return position[1] - position[0]
        left = 1
        right = position[-1] - position[0]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if self.placeWithMinDistance(position, mid, m):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans

    def placeWithMinDistance(self, position: list[int], gap: int, balls: int) -> bool:
        balls -= 1
        idx = 1
        lastIdx = 0
        while balls > 0:
            if idx >= len(position):
                return False
            if position[idx] - position[lastIdx] >= gap:
                # place the ball
                balls -= 1
                lastIdx = idx
                idx += 1
            else:
                idx += 1

        return True