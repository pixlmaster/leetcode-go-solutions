import bisect




class Solution:
    def insort_unique(self, sorted_list, item):
        """Insert `item` into `sorted_list` in sorted order if it's not already present."""
        pos = bisect.bisect_left(sorted_list, item)
        if pos == len(sorted_list) or sorted_list[pos] != item:
            bisect.insort(sorted_list, item)
        
    def nthUglyNumber(self, n: int) -> int:
        """
        current = 1
        next2 = current*2
        next3 = current*3
        next5 = current*5
        least becomes current

        """
        current = 1
        elems = [1]
        itr = 0
        for i in range(n):
            self.insort_unique(elems, current * 2)
            self.insort_unique(elems, current * 3)
            self.insort_unique(elems, current * 5)
            itr += 1
            current = elems[itr]

        # print(elems)
        return elems[n - 1]
