class Solution:
    # TC: O(n), MC: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxSubstring = 0
        for i in range(len(s)):
            dict = {}
            k = i
            
            while k<len(s) and s[k] not in dict:
                dict[s[k]] = k
                k+=1
            
            if len(s[i:k])>maxSubstring:
                maxSubstring = len(s[i:k])
            
        return maxSubstring
