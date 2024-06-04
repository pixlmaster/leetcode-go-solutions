class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [(nums1[0]+nums2[0],(0,0))]
        len1 = len(nums1)
        len2 = len(nums2)
        visited= set()
        visited.add((0,0))

        ans = []
        while k> 0 and len(pq) >0:
            sum, (i, j) = heappop(pq)
            ans.append([nums1[i],nums2[j]])

            if i+1<len1 and not (i+1,j) in visited:
                heappush(pq,[nums1[i+1] + nums2[j],(i+1,j)])
                visited.add((i+1,j))

            if j+1<len2 and not (i,j+1) in visited:
                heappush(pq,[nums1[i] + nums2[j+1],(i,j+1)])
                visited.add((i,j+1))

            
            k-=1
        
        return ans




        