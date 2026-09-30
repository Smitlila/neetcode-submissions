class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n - 1
        mini = float("inf")

        while l <= h:
            m = (l + h)//2
            

            if nums[m] <= nums[h]:
                mini = min(mini, nums[m])
                h = m - 1
            else:
                mini = min(mini, nums[m])
                l = m + 1
            
        return mini
        