'''
Substring problem: how to determine whether a string is a substring of another string

example:
s1 = 'abcde'
s2 = 'cd'
'''

class Solution:
    def substring(self, s1, s2):
        if not s2:
            return False
        i = 0
        while i <= len(s1)-len(s2):
            if s1[i:i+len(s2)] == s2:
                return True
            i += 1
        return False

if __name__ == '__main__':
    s1 = 'abbbac'
    s2 = 'bb'
    o = Solution()
    print(o.substring(s1, s2))