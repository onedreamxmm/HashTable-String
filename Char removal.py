'''
Remove all leading/trailing and duplicate empty spaces(only leave one empty space if duplicated spaces happen) from the input string.

example:
input = '___abc__ed___ef___';
output = 'abc_ed_ef'
'''

class Solution:
    def removeSpace(self, str):
        res = ''
        j = 0
        while True:
            while j < len(str) and str[j] != ' ':
                res += str[j]
                j += 1
            while j < len(str) and str[j] == ' ':
                j += 1
            if j == len(str):
                break
            if res:
                res += ' '
        return res

if __name__ == '__main__':
    str1 = '  I   love  Python and Leetcode   '
    o = Solution()
    print(o.removeSpace(str1))


