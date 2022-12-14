class Solution:
    # TC: O(nlogn), MC: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        sortedPrices = sorted(prices, reverse=True)
        
        maxProfitForEveryElement = []
        
        for i in range(len(prices)):
            sortedPrices.remove(prices[i])
            
            if len(sortedPrices) and sortedPrices[0]>prices[i]:
                maxProfitForEveryElement.append(sortedPrices[0]-prices[i])
            else:
                maxProfitForEveryElement.append(0)
            
        return max(maxProfitForEveryElement)
