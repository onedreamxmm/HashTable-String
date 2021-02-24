'''
remove duplicated and adjacent letters(leave only one letter in each duplicated section) in a string.

example:
input:'aabb__cc'
output:'ab_c'
'''

class Solution:
    def removeDuplicate(self, str):
        res = ''
        for letter in str:
            if not res or letter != res[-1]:
                res += letter
        return res

if __name__ == '__main__':
    str1 = 'aabb  cc'
    str2 = ''
    o = Solution()
    print(o.removeDuplicate(str1))
    print(o.removeDuplicate(str2))