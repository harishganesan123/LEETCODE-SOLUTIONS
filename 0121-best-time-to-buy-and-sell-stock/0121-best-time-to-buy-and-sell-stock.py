class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans =0
        mi=inf
        for i in prices:
            ans = max(ans, i-mi)
            mi=min(mi,i)
        return(ans)