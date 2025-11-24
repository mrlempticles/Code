class Solution:
    def maximumTotalDamage(self, power):
        from collections import Counter
        
        freq = Counter(power)
        items = sorted(freq.items())  # (value, frequency)
        n = len(items)
        
        # Precompute total damage for each value
        damage = [v * c for v, c in items]
        
        # Precompute prev index for compatibility (values differ by > 2)
        prev = [0] * n
        for i in range(n):
            # binary search for last valid j
            lo, hi = 0, i - 1
            best = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if items[mid][0] < items[i][0] - 2:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            prev[i] = best
        
        # DP
        dp = [0] * n
        for i in range(n):
            # Option 1: skip current
            not_take = dp[i - 1] if i > 0 else 0
            
            # Option 2: take current + dp[prev[i]]
            take = damage[i]
            if prev[i] != -1:
                take += dp[prev[i]]
            
            dp[i] = max(take, not_take)
        
        return dp[-1]
