class Solution:
    # TC: O(N), MC: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        xorVal = nums[0]
        for i in range(1,len(nums)):
            xorVal = xorVal^nums[i]
        return xorVal
