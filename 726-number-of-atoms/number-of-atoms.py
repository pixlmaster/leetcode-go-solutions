import string
from collections import deque


class Solution:
    openPar = "("
    closePar =")"


    def countOfAtoms(self, formula: str) -> str:
        """
        1. stack
        2. stack -> (
        3.if ( or name put in stack
        4. when ecounter close -> process all elements until open in the stack
        """
        n = len(formula)
        stack = deque()
        itr = 0
        freqMap = {}
        # iterate over the characters
        for itr in range(len(formula)):

            # INSERTION
            char = formula[itr]
            # either form a number or a string
            if char in string.ascii_uppercase:
                # add the capital letter
                currElement = char
                itr+=1
                # add following small letters if any
                while itr <n and formula[itr] in string.ascii_lowercase:
                    currElement += formula[itr]
                    itr += 1
                # terminate condition
                if itr >= n:
                    # string ended
                    stack.append((currElement,1))
                    continue
                if not formula[itr].isdigit() :
                    stack.append((currElement,1))
                else :
                    number = ""
                    while itr < n and formula[itr].isdigit():
                        number += formula[itr]
                        itr += 1
                    stack.append((currElement,int(number)))
            elif char == self.openPar:
                stack.append((char,1))
            elif char == self.closePar:
                itr += 1
                # freq = 1
                if itr >= n:
                    freq = 1
                else :
                    if not formula[itr].isdigit() :
                        freq = 1
                    else :
                        number = ""
                        while itr< n and formula[itr].isdigit():
                            number += formula[itr]
                            itr += 1
                        freq = int(number)
                popped = stack.pop()
                tempq = deque()
                while popped[0] != self.openPar:
                    modPopped = (popped[0], freq*popped[1])
                    tempq.append(modPopped)
                    popped = stack.pop()
                while tempq:
                    stack.append(tempq.pop())

        while stack:
            popped = stack.pop()
            if popped[0] == self.openPar:
                continue
            if popped[0] not in freqMap:
                freqMap[popped[0]] = popped[1]
            else:
                freqMap[popped[0]] += popped[1]
        # print(freqMap)
        freqList = list(freqMap.keys())
        freqList.sort()
        # print(freqList)
        
        ans = ""
        for elem in freqList:
            if freqMap[elem] !=1:
                ans += elem + str(freqMap[elem])
            else:
                ans += elem    
        return ans
                