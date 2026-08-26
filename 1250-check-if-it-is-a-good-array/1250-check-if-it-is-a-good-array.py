class Solution(object):

    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = nums[0]

        for i in range(1, len(nums)):
            g = gcd(g, nums[i])

        return g == 1