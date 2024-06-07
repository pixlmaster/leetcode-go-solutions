class Map:
    def __init__(self):
        self.hmap ={}
        
    def constructHMap(self,hand: list[int]) -> None:
        for itr,h in enumerate(hand) :
            if h not in self.hmap:
                self.hmap[h] = set([itr])
            else:
                self.hmap[h].add(itr)

    def find(self, elem: int) -> bool:
        if elem not in self.hmap:
            return False
        return True
        
    def get(self, elem: int) -> int:
        if self.find(elem):
            return self.hmap[elem]
        return None
    
    def removeFromSet(self, elem: int) -> int:
        tempset = self.get(elem)
        # print(self.hmap)
        # print(elem, tempset)
        if tempset and len(tempset) > 0 :
            ans = tempset.pop()
            if len(tempset) == 0:
                self.delete(elem)
            return ans
        return None
        
    def delete(self, elem: int):
        del self.hmap[elem]

class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        # if len is not divisible by groupsize, return false
        n = len(hand)
        if n%k >0 :
            return False
        deleted = float("inf")
        # sort the array and crete a map, mapping element to an index
        # pick the smallest element, pick smallest+1, pick smallest+2, if not avail -> return false
        # delete the picked elements from the(by modifying their value to inf)
        # hand = sorted(hand)
        hashMap = Map()
        hashMap.constructHMap(hand)
        for elem in hand:
            # deleted element skip
            if elem == deleted:
                continue
            while hashMap.find(elem-1):
                elem -=1

            smallest=elem
            sidx = hashMap.removeFromSet(smallest)
            hand[sidx] = deleted
            # pick the next k consequtive elements
            for add in range(1,k):
                toSearch = smallest+add
                # next consequtive element not availaible
                if not hashMap.find(toSearch):
                    return False
                # found next element, delete it from the availaible
                idx = hashMap.removeFromSet(toSearch)
                # print(smallest,hand[idx])
                hand[idx] = deleted
        
        return True
                

    

