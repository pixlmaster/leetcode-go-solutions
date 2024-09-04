from bisect import bisect_left, bisect_right
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Solution:
    def turnLeft(self, dir : Direction) -> Direction:
        if dir != Direction.NORTH:
            return Direction(dir.value -1)
        else:
            return Direction(Direction.WEST)

    def turnRight(self, dir : Direction) -> Direction:
        if dir != Direction.WEST:
            return Direction(dir.value +1)
        else:
            return Direction(Direction.NORTH)

    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        """
        simply simulate
        """
        obstaclesR = {}
        obstaclesC = {}
        for obstacle in obstacles:
            r = obstacle[0]
            c = obstacle[1]
            if r not in obstaclesR:
                obstaclesR[r] = [c]
            else:
                obstaclesR[r].append(c)
            if c not in obstaclesC:
                obstaclesC[c] = [r]
            else:
                obstaclesC[c].append(r)

        for key in obstaclesR.keys():
            obstaclesR[key].sort()

        for key in obstaclesC.keys():
            obstaclesC[key].sort()

        x = 0
        y = 0
        direction = Direction.NORTH
        ans = 0
        for command in commands:
            if command == -2:
                # Turn left
                print("turn left")
                direction = self.turnLeft(direction)
            elif command == -1:
                print("turn right")
                direction = self.turnRight(direction)
            else :
                print("before traversal, ", x, y)
                x, y = self.traverse(x,y,direction,obstaclesR,obstaclesC, command)
                print("after traversal, ", x, y)
                ans = max(ans, x**2 + y**2)

        return ans

    def traverse(self,x : int,y: int,direction : Direction,obstaclesR : dict[int,list[int]],obstaclesC : dict[int,list[int]], steps: int):
        if direction == Direction.NORTH:
            if x in obstaclesR:
                arr  = obstaclesR[x]
                idx = bisect_right(arr, y)
                if idx == len(arr):
                    return x, y + steps
                else:
                    return x ,min(y+steps,arr[idx]-1)
            else:
                return x, y + steps

        elif direction == Direction.SOUTH:
            if x in obstaclesR:
                arr  = obstaclesR[x]
                idx = bisect_left(arr, y)
                if idx == 0:
                    return x, y - steps
                else:
                    return x ,max(y-steps,arr[idx-1]+1)
            else:
                return x, y - steps

        elif direction == Direction.EAST:
            if y in obstaclesC:
                arr = obstaclesC[y]
                idx = bisect_right(arr, x)
                if idx == len(arr):
                    return x + steps, y
                else:
                    return min(arr[idx]-1, x +steps), y
            else:
                return x + steps, y

        elif direction == Direction.WEST:
            if y in obstaclesC:
                arr = obstaclesC[y]
                idx = bisect_left(arr, x)
                if idx == 0:
                    return x - steps, y
                else:
                    return max(arr[idx-1]+1, x - steps), y
            else:
                return x - steps, y
