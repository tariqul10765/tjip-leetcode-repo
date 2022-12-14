class Solution:
    # TC: O(n), MC: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        
        maximum = 0
        element = nums[0]
        for ele in dict:
            if dict[ele] > maximum:
                maximum = dict[ele]
                element = ele
                
        return element
