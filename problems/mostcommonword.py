import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        mostCommon = count.most_common(1)
        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))