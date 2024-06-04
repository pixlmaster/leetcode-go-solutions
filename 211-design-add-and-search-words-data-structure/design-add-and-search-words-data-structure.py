class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if not letter in curr:
                curr[letter] = {}
            curr=curr[letter]
        curr["*"] = ""

    def search(self, word: str) -> bool:
        return self.search2(word,self.root)

            
    def search2(self, word:str, curr) -> bool:
        # print("searching", word)
        # print("curr ", curr)
        for idx,letter in enumerate(word):
            if letter != "." and not letter in curr:
                return False
            if letter == ".":
                for char in curr:
                    if self.search2(char+word[idx+1:],curr):
                        return True
                return False
            curr = curr[letter]
        
        if "*" in curr:
            return True
        return False
                    
                 



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)