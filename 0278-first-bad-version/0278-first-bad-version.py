# The isBadVersion API is already defined for you.
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid      # mid might be the first bad one
            else:
                left = mid + 1   # first bad is on the right
        
        return left
