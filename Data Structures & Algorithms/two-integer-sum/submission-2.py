class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        #set a hashmap for all visited indexes
        has = {}

        
        for i, n in enumerate(nums):
            a = target - n

            if a in has:
                return [has[a], i]
            has[n] = i
        