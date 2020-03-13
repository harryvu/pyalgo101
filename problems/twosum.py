"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example
-------
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum_bruteforce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, ival in enumerate(nums):
            for j, jval in enumerate(nums[i+1:],i+1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        

    def twoSum_hashtable_2_pass(self, nums, target):
        
        # build the hash table for look up later
        my_hashtable = {}
        for i, ival in enumerate(nums):
            my_hashtable[ival] = i
        
        for j, jval in enumerate(nums):
            complement = target - nums[j]
            if complement in my_hashtable and my_hashtable[complement] != j:
                return [j, my_hashtable[complement]]


nums = [2, 7, 11, 15]
target = 9
nums = [3,2,4]
target = 6

solution = Solution()
print(solution.twoSum_bruteforce(nums, target))
print(solution.twoSum_hashtable_2_pass(nums, target))