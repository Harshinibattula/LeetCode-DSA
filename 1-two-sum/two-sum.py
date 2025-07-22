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

            

       