'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:
Input: s = "a", t = "a"
Output: "a"

Constraints:
1 <= s.length, t.length <= 105
s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(n) time?
'''
from collections import Counter
class Solution:
    def miniWindow(self, s, t):
        if not s or not t:
            return ''
        target_letter = Counter(t)    #O(T)
        target_len = len(t)
        start = 0
        res = ''
        for end, char in enumerate(s):  #O(S)
            if target_letter[char] > 0:
                target_len -= 1
            target_letter[char] -= 1
            if target_len == 0:
                while target_letter[s[start]] < 0:
                    target_letter[s[start]] += 1
                    start += 1
                if not res or end-start+1 < len(res):
                    res = s[start: end+1]
                target_letter[s[start]] += 1
                target_len += 1
                start += 1
        return res





