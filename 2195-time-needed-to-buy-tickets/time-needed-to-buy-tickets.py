class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = k+1
        for i in range(k+1):
            tickets[i]-=1
        # print(tickets)
        buy = tickets[k]
        if buy == 0 :
            return ans
        for ticket in tickets:
            ans += min(ticket,buy)
        
        return ans