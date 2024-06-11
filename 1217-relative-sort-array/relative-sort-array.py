class Solution:

    def compare(self, a : int,b : int) -> int:
        idxa = self.hmap[a]
        idxb = self.hmap[b]
        if idxa < idxb:
            return -1
        
        return 1
        

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        self.hmap = {}

        for i,num in enumerate(arr2):
            self.hmap[num] = i

        suffix = []
        prefix = []

        for num in arr1:
            if num in self.hmap:
                prefix.append(num)
            else:
                suffix.append(num)


        
        prefix = sorted(prefix,key=cmp_to_key(self.compare))
        suffix = sorted(suffix)

        prefix.extend(suffix)
        return prefix