class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        zipNames = zip(names, heights)
        zipNames = sorted(zipNames, key=lambda x: x[1])
        n = len(names)
        for i,zipName in enumerate(zipNames):
            names[n-i-1] = zipName[0]
        return names
        