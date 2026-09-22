class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Optimal: Two pointer
        n = len(nums)

        #sort the array first
        nums.sort()
        res = []

        #get the 3 value getting from last element1st and 2nd
        for i, a in enumerate(nums):
            #if the cur and prev elements are same we will skip it casue no duplicates are allowed
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = n - 1

            while l<r:
                total = a + nums[l] + nums[r]
                # if total is more then 0 we will move the right pointer 
                if total > 0:
                    r -= 1
                #if total is less then 0 we will move left pointer
                elif total < 0:
                    l += 1
                # else we will add it to the list and increment the left pointer 
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    # check the cur and prev and if same move further 
                    while nums[l] == nums[l- 1] and l<r:
                        l += 1
        return res

        #Brute Force : using 3 for loops, t(n) = O(n3), s(n) = O(n)
        # n = len(nums)
        # mySet = set()

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             total = nums[i] + nums[j] + nums[k]
        #             if total == 0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 temp.sort()
        #                 mySet.add(tuple(temp))
        
        # return [list(ans) for ans in mySet]
