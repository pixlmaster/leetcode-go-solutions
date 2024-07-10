class Solution:
    prevDir = "../"
    dotChar = "."
    def minOperations(self, logs: list[str]) -> int:
        """
        1. iterate through the logs
        2. if "../", level--(if level>0)
        3. if "./", remain in the same folder
        4. if "x/" level+=1
        """
        level = 0
        for log in logs:
            if log == self.prevDir:
                if level > 0:
                    level -= 1
            elif log[0] != self.dotChar:
                level += 1
        return level