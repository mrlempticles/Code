class Solution(object):
    def minimizeMax(self, nums, p):
        nums.sort()

        def can_form_pairs(diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= diff:
                    count += 1
                    i += 2  # skip next since each index used once
                else:
                    i += 1
            return count >= p

        # binary search for minimum possible diff
        left, right = 0, nums[-1] - nums[0]
        res = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
  