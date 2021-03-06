'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:
Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:
Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Complexity Analysis
Time complexity: O(N), where N is a number of characters in the input string.
Space complexity: O(N), to store the result of split by spaces.
'''


class Solution:
    def reverseWords1(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


    def reverseWords2(self, s: str) -> str:
        def trimString(str):
            i, j = 0, 0
            wordCount = 0
            while True:
                while j < len(str) and str[j] == ' ':
                    j += 1
                if j == len(str):
                    break
                if wordCount > 0:
                    str[i] = ' '
                    i += 1
                while j < len(str) and str[j] != ' ':
                    str[i] = str[j]
                    i += 1
                    j += 1
                wordCount += 1
            return str[:i]

        def reverseString(str, l, r):
            while l < r:
                str[l], str[r] = str[r], str[l]
                l += 1
                r -= 1

        str = []
        for ch in s:
            str.append(ch)
        str = trimString(str)
        reverseString(str, 0, len(str)-1)
        i = 0
        while i < len(str):
            j = i
            while j < len(str) and str[j] != ' ':
                j += 1
            reverseString(str, i, j-1)
            i = j + 1
        return ''.join(str)


if __name__ == '__main__':
    string1 = '  I   love     Python    '
    string2 = ''
    o = Solution()
    print(o.reverseWords1(string1))
    print(o.reverseWords1(string2))
    print(o.reverseWords2(string1))
    print(o.reverseWords2(string2))
