class Solution:
    def maxSumDivThree(self, nums):
        nums1 = []
        nums2 = []
        total = 0

        for x in nums:
            total += x
            if x % 3 == 1:
                nums1.append(x)
            elif x % 3 == 2:
                nums2.append(x)

        nums1.sort()
        nums2.sort()

        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            remove1 = nums1[0] if nums1 else float('inf')
            remove2 = nums2[0] + nums2[1] if len(nums2) >= 2 else float('inf')
            return total - min(remove1, remove2)
        else:  # total % 3 == 2
            remove1 = nums2[0] if nums2 else float('inf')
            remove2 = nums1[0] + nums1[1] if len(nums1) >= 2 else float('inf')
            return total - min(remove1, remove2)
