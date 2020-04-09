"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            # base case
            return [nums]
        
        # recursive case
        answers = []
        for i in range(len(nums)):
            # create new list call newNums that have the same elements except the ith-element
            newNums = nums[:i] + nums[i+1:]
            for p in self.permute(newNums):
                answers.append([nums[i]] + p)
        return answers

    def permute3(self, word):
        if len(word) == 1:
            return [word]

        char = word[0]
        result = []
        for perm in self.permute3(word[1:]):
            for i in range(len(perm) + 1):
                result.append(perm[:i] + [char] + perm[i:])
        
        return result
    
    def permute2(self, lst):
        if len(lst) == 1:
            # base case
            yield [lst]
        
        # recursive case
        for i in range(len(lst)):
            # create new list call newNums that have the same elements except the ith-element
            newNums = lst[:i] + lst[i+1:]
            for p in self.permute2(newNums):
                yield [lst[i]] + p


nums = list('123')
sol = Solution()
print(sol.permute(nums))
#print(sol.permute3(nums))

# for i in sol.permute3(nums):
#     print(i)