class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # At most 2 elements can appear more than n/3 times.
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        # Phase 1: find candidates (Boyer-Moore voting, generalized)
        for n in nums:
            if cand1 == n:
                count1 += 1
            elif cand2 == n:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: verify candidates actually appear > n/3 times
        result = []
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > len(nums) // 3:
                result.append(cand)

        return result