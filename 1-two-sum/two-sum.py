#O(n^2)---brute force 
# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             x = target - nums[i]
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == x:
#                     return [i, j]

#O(n)
class Solution:
    def twoSum(self,nums,target):
        seen={}
        for i,val in enumerate(nums):
            complement=target-val
            if complement in seen:
                return [seen[complement],i]
            else:
                seen[val]=i

            

       