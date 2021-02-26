'''
'I love Yahoo' -> 'Yahoo love I'

'''

class Solution:
    def reverseString(self, s):
        def helper(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        helper(0, len(s)-1)   #reverse the whole string
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1
            helper(i, j-1)
            i = j + 1
        return s

if __name__ == '__main__':
    s1 = ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'a', 'h', 'o', 'o']
    s2 = []
    o = Solution()
    print(o.reverseString(s1))
    print(o.reverseString(s2))







