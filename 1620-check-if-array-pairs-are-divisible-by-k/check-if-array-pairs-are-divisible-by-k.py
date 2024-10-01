class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        hmap = {}
        for i in range(n):
            arr[i] = arr[i]%k
            if arr[i] in hmap:
                hmap[arr[i]] += 1
            else:
                hmap[arr[i]] = 1
        if 0 in hmap:
            if hmap[0] % 2 !=0:
                return False
            del(hmap[0])

        for key,val in hmap.items():
            if k-key not in hmap or hmap[k-key] !=val:
                return False

        return True


