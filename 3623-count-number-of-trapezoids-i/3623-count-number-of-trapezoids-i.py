class Solution:
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        from collections import defaultdict
        
        # Count points on each horizontal line (same y)
        level = defaultdict(int)
        for x, y in points:
            level[y] += 1
        
        horiz_segments = []
        total_segments = 0
        
        # Count horizontal line segments on each level
        for y in level:
            k = level[y]
            if k >= 2:
                seg = k * (k - 1) // 2   # C(k,2)
                horiz_segments.append(seg)
                total_segments += seg
        
        # Need at least two horizontal segments to form a trapezoid
        if total_segments < 2:
            return 0
        
        # Total ways to choose two segments
        total_pairs = total_segments * (total_segments - 1) // 2
        
        # Subtract invalid pairs: two segments from the same y-level
        same_level_pairs = 0
        for seg in horiz_segments:
            same_level_pairs += seg * (seg - 1) // 2
        
        return (total_pairs - same_level_pairs) % MOD
