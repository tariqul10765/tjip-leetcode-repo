class Solution:
    # TC: O(n^2), MC: O(1)
    # def largestNumber(self, nums: List[int]) -> str:
    #     for i in range(len(nums)):
    #         nums[i] = str(nums[i])
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if nums[i]+nums[j]>nums[j]+nums[i]:
    #                 nums[i],nums[j] = nums[j],nums[i] 
        
    #     return str(int(''.join(nums)))

    # TC: O(nlogn), MC: O(1)
    def compareNumber(self, num1, num2):
        if num1+num2 <= num2+num1:
            return 1
        else:
            return -1

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        sortedNums = sorted(nums, key = cmp_to_key(self.compareNumber))
        
        return str(int(''.join(sortedNums)))
