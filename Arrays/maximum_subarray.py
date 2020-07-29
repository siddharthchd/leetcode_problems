class Solution:
    def maxSubArray(self, nums):
        current_sum = best_sum = 0
        for x in nums:
            current_sum += x
            current_sum = max(0, current_sum)
            best_sum = max(best_sum, current_sum)
        return best_sum

s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
