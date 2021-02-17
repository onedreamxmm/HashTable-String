'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Example 4:

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.


Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)    #time complexity: o(n)
        n = len(nums)
        for i in range(n+1):    #time complexity: o(n)
            if i not in num_set:  #time complexity: o(1)
                return i
'''
Complexity Analysis
Time complexity : O(n)
Space complexity : O(n)
nums contains n−1 distinct elements, so it costs O(n) space to store a set containing all of them.
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):   #O(n)
            missing ^= i ^ num     #O(1)
        return missing
'''
Complexity Analysis
Time complexity : O(n)
Assuming that XOR is a constant-time operation, this algorithm does constant work on nn iterations, so the runtime is overall linear.
Space complexity : (1)
This algorithm allocates only constant additional space.
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  #O(1)
        actual_sum = sum(nums)       #O(n)
        return expected_sum - actual_sum

'''
Complexity Analysis
Time complexity : O(n)
Although Gauss' formula can be computed in O(1) time, summing nums costs us O(n) time, so the algorithm is overall linear. Because we have no information about which number is missing, an adversary could always design an input for which any algorithm that examines fewer than n numbers fails. Therefore, this solution is asymptotically optimal.
Space complexity : O(1)
This approach only pushes a few integers around, so it has constant memory usage.
'''