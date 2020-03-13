"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        start = 0
        end = 0
        for i, val in enumerate(s):
            len1 = self.__expandFromCenter(s, i, i)
            len2 = self.__expandFromCenter(s, i, i+1)
            len = max(len1, len2)

            if len > end - start:
                start = i - (len -1) // 2
                end = i + len // 2

        return s[start:end+1]
    
    def __expandFromCenter(self, s, left, right):
        while (left >= 0 and right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1

        return right - left - 1

mystr = "sdaacabacccaafdracecardfgdf"
sol = Solution()
print(sol.longestPalindrome(mystr))