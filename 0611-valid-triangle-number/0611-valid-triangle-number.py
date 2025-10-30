class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        n = len(nums)

        # Fix the largest side one by one
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                # If sum of smaller sides is greater than the largest, triangle is possible
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count
   