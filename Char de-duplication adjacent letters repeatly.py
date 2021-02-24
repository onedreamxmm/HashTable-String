class Solution:
    def removeDuplicate(self, str):
        stack = []
        i = 0
        while i < len(str):
            if stack and str[i] == stack[-1]:
                while str[i] == stack[-1]:
                    i += 1
                stack.pop()
            else:
                stack.append(str[i])
                i += 1
        return ''.join(stack)

if __name__ == '__main__':
    str1 = 'abbbacode'
    str2 = ''
    str3 = 'aaabbbaccdc'
    o = Solution()
    print(o.removeDuplicate(str1))
    print(o.removeDuplicate(str2))
    print(o.removeDuplicate(str3))