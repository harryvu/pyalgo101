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
    def permute(self, lst):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(lst) == 0:
            # base case
            return []
        elif len(lst) == 1:
            # base case
            return [lst]
        else:
            # recursive case
            answers = []
            for i in range(len(lst)):
                # create new list call newNums that have the same elements except the ith-element
                newNums = lst[:i] + lst[i+1:]
                for p in self.permute(newNums):
                    answers.append([lst[i]] + p)
            return answers

    def permute2(self, lst):
        """
        :type nums: List[int]
        :rtype: generator[List[int]]
        """

        if len(lst) == 0:
            # base case
            yield []
        elif len(lst) == 1:
            # base case
            yield [lst]
        else:
            # recursive case
            answers = []
            for i in range(len(lst)):
                # create new list call newNums that have the same elements except the ith-element
                newNums = lst[:i] + lst[i+1:]
                for p in self.permute(newNums):
                    yield [lst[i]] + p

nums = list('123')
sol = Solution()
print(sol.permute(nums))

for i in sol.permute2(nums):
    print(i)