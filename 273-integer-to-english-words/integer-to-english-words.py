class Solution:
    strEdgeCase = {
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty"
    }

    strOnes = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    strTens = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety"
    }

    strBillion = "Billion"
    strMillion = "Million"
    strThousand = "Thousand"
    strHundred = "Hundred"

    digOne = 1
    digTen = 2
    digHundred = 3
    digThousand = 4
    digMillion = 7
    digBillion = 10

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.strOnes[num]
        # handle edge cases
        snum = str(num)
        n = len(snum)
        numOnes = -1
        numTens = -1
        numHundreds = -1
        numThousands = -1
        numMillions = -1
        numBillions = -1

        if n >= self.digOne:
            numOnes = int(snum[-self.digOne:])

        if n >= self.digTen:
            numTens = int(snum[-self.digTen:-self.digOne])

        if n >= self.digHundred:
            numHundreds = int(snum[-self.digHundred:-self.digTen])

        if n >= self.digThousand:
            numThousands = int(snum[-self.digThousand - 2:-self.digHundred])

        if n >= self.digMillion:
            numMillions = int(snum[-self.digMillion - 2:-self.digThousand-2])

        if n >= self.digBillion:
            numBillions = int(snum[-self.digBillion - 2:-self.digMillion-2])

        # print("ones", numOnes)
        # print("tens", numTens)
        # print("hundred", numHundreds)
        # print("thousand", numThousands)
        # print("million", numMillions)
        # print("billion", numBillions)
        ans = ""

        if numBillions > 0:
            ans += self.numberToWords(numBillions) + " " + self.strBillion + " "

        if numMillions > 0:
            ans += self.numberToWords(numMillions) + " " + self.strMillion + " "

        if numThousands > 0:
            ans += self.numberToWords(numThousands) + " " + self.strThousand + " "

        if numHundreds > 0:
            ans += self.strOnes[numHundreds] + " " + self.strHundred + " "

        if numTens > 0:
            if numTens == 1:
                temp = numTens * 10 + numOnes
                ans += self.strEdgeCase[temp]
                return ans
            ans += self.strTens[numTens] + " "

        if numOnes > 0:
            ans += self.strOnes[numOnes]

        return ans.strip()
