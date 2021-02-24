'''
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
Example 1:
Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:
Input: s = "aeiou"
Output: ""

'''


class Solution:
    def removeVowels(self, s: str) -> str:
        res = ''
        for letter in s:
            if letter not in 'aeiou':
                res += letter
        return res


