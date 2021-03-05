'''
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


'''

class Solution:
    def longestSubstring1(self, s):
        res = 0
        i = 0
        map = {}
        for j in range(len(s)):
            if s[j] in map:
                i = max(map[s[j]], i)
            res = max(res, j-i+1)
            map[s[j]] = j + 1
        return res

    def longestsubstring2(self, s):
        res = start = 0
        usedChar = {}
        for i, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            res = max(res, i-start+1)
            usedChar[char] = i
        return res
