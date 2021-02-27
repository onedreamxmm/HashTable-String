'''
remove all leading/trailing and duplicate empty spaces

'''

'''
Remove all leading/trailing and duplicate empty spaces(only leave one empty space if duplicated spaces happen) from the input string.

example:
input = '___abc__ed___ef___';
output = 'abc_ed_ef'
'''

class Solution:
    def removeSpace(self, str):
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


if __name__ == '__main__':
    str = []
    for ch in '  I   love  Python and Leetcode   ':
        str.append(ch)
    print(str)
    o = Solution()
    print(o.removeSpace(str))


