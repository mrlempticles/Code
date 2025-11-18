class Solution:
    def findSmallestInteger(self, nums, value):
        from collections import Counter
        
        freq = Counter([x % value for x in nums])
        
        mex = 0
        while True:
            r = mex % value
            if freq[r] > 0:
                freq[r] -= 1
                mex += 1
            else:
                return mex
