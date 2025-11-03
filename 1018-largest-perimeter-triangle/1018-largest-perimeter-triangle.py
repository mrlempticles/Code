class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the sides in descending order
        nums.sort(reverse=True)
        
        # Check every triplet
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            # Triangle condition: sum of smaller two sides > largest side
            if b + c > a:
                return a + b + c
        
        # If no valid triangle found
        return 0
