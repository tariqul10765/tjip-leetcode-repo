class Solution:
    # TC: O(n), MC: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        res=[]
        
        mul=1
        prefix.append(mul)
        for i in range(1,len(nums)):
            mul*=nums[i-1]
            prefix.append(mul)
        
        
        mul=1
        postfix.append(mul)
        for i in range(len(nums)-2,-1,-1):
            mul*=nums[i+1]
            postfix.append(mul)
        
        k=len(nums)-1
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[k])
            k-=1
        
        return res
