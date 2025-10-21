class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Step 1: Sort array
        res = []
        n = len(nums)

        # Step 2: First two loops to fix a and b
        for i in range(n - 3):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate values for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Step 3: Two-pointer search for remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1  # Need bigger sum
                    else:
                        right -= 1  # Need smaller sum

        return res