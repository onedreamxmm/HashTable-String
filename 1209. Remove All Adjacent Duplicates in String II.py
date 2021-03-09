'''
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.



Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.

'''

class Solution:
    def removeDuplicates(self, s, k):
        count = []
        for ch in s:
            if not count or count[-1][0] != ch:
                count.append([ch, 1])
            else:
                count[-1][1] += 1
                if count[-1][1] == k:
                    count.pop()
        return ''.join(ch * n for ch, n in count)

if __name__ == '__main__':
    s1 = 'deeedbbcccbdaa'
    k1 = 3
    s2 = 'pbbcggttciiippooaais'
    k2 = 2
    o = Solution()
    print(o.removeDuplicates(s1, k1))
    print(o.removeDuplicates(s2, k2))
