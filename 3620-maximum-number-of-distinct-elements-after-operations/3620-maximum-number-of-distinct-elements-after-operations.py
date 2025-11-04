class Solution(object):
    def maxDistinctElements(self, nums, k):
        nums.sort()
        count = 0
        next_available = -float('inf')
        
        for a in nums:
            low = a - k
            high = a + k
            
            # Choose the smallest possible distinct value >= next_available
            if next_available < low:
                next_available = low
            
            if next_available <= high:
                count += 1
                next_available += 1  # move to next unused number
                
        return count

        