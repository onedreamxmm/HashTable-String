'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

time complexity: O(n log k)
space complexity: O(n)

参考：
https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)

Read the comment in https://github.com/python/cpython/blob/master/Lib/heapq.py before line 461. nsmallest is implemented O(nlgk).
If you are interested in that, read http://code.activestate.com/recipes/577573-compare-algorithms-for-heapqsmallest/ for more details
'''

import collections
import heapq
class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        return heapq.nsmallest(k, count, key=lambda w: (-count[w], w))


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    o = Solution()
    print(o.topKFrequent(words, k))