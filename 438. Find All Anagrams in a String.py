'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        res = []
        ns, np = len(s), len(p)
        pCount = Counter(p)
        sCount = Counter()
        for i, ch in enumerate(s):
            sCount[ch] += 1
            if i >= np:
                if sCount[s[i - np]] == 1:
                    del sCount[s[i - np]]
                else:
                    sCount[s[i - np]] -= 1
            if pCount == sCount:
                res.append(i - np + 1)
        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    o = Solution()
    print(o.findAnagrams(s, p))