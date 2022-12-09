class Solution:
    # TC: O(n), MC: (n)
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        
        # maxLeft = height[i]
        maxRight = [0]*len(height)
        ma = 0
        
        for i in range(len(height)-1, -1, -1):
            maxRight[i] = ma
            
            if ma<height[i]:
                ma = height[i]
        
        ma = 0
        totalSum = 0
        
        for i in range(len(height)):
            minLen = min(maxRight[i],ma)
            totalSum+=(minLen-height[i]) if (minLen-height[i])>=0 else 0
            
            if ma<height[i]:
                ma = height[i]
            
            
        
        return totalSum
