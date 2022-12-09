class Solution:
    # TC: O(n), MC: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxLen=0
        
        for n in nums:
            if n-1 not in numSet:
                length=0
                while (n+length) in numSet:
                    length+=1
                maxLen=max(maxLen,length)
        return maxLen
