class Solution:
    def commonNumber1(self, nums1, nums2):
        set1 = set(nums1)    #O(n)
        set2 = set(nums2)    #O(m)
        return list(set1 & set2)

    def commonNumber2(self, nums1, nums2):
        i, j =0, 0
        res = []
        while i < len(nums1) and j < len(nums2):  #O(n+m)
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

    def commonNumber3(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        res = []
        if n <= m:
            for i in range(n):         #O(n)
                self.BS(nums1[i], nums2, res)   #O(log m)
        else:
            for j in range(m):
                self.BS(nums2[j], nums1, res)
        return res

    def BS(self, target, nums, res):
        l , r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else: return res.append(target)



if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [4, 5, 6, 7, 8]
    nums3 = [1, 2, 3, 4]
    nums4 = [5, 6, 7, 8]
    o = Solution()
    print(o.commonNumber1(nums1, nums2), end = ' ')
    print(o.commonNumber2(nums1, nums2), end = ' ')
    print(o.commonNumber3(nums1, nums2))
    print(o.commonNumber1(nums3, nums4), end = ' ')
    print(o.commonNumber2(nums3, nums4), end = ' ')
    print(o.commonNumber3(nums3, nums4))