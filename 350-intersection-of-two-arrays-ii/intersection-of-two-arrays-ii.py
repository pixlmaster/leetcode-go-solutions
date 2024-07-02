class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        ans = []
        for elem in nums1:
            if elem not in hmap:
                hmap[elem] = 1
            else:
                hmap[elem]+=1
        
        for elem in nums2:
            if elem not in hmap:
                continue
            if hmap[elem]>0:
                ans.append(elem)
                hmap[elem]-=1
        
        return ans