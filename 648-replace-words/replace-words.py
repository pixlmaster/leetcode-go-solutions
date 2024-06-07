class Trie:
    end = "*"
    def __init__(self):
        self.root = {}
    
    # inserts word into trie
    def insert(self, word:str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr[self.end] = {}
    
    # searches for a prefix present in the given word
    def searchPrefix(self, word:str) -> str:
        ans = ""
        curr = self.root
        for letter in word:
            # no prefix found and trie and word diverged
            if letter not in curr:
                if self.end in curr:
                    return ans
                else :
                    return ""
            # early prune for the smallest prefix
            if self.end in curr:
                return ans

            curr = curr[letter]
            ans+=letter
        # case where word is longer than the trie prefixes, loop will end but only return if prefix ends here
        if self.end in curr:
            return ans
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        split = sentence.split()
        n = len(split)
        ans =""
        for i,word in enumerate(split):
            prefix = trie.searchPrefix(word)
            # print(word,prefix)
            if len(prefix) ==0 :
                ans +=word
            else:
                ans+=prefix
            if i <n-1:
                ans+=" "
                
        return ans