class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        fSet = set(folder)
        for f in folder:
            for i in range(len(f)):
                if i>0 and f[i] == "/":
                    # print(f, "checking", f[:i],"in ", fSet)
                    if f[:i] in fSet:
                        fSet.remove(f)
                        break
        return list(fSet)