class Solution:
    def minCost(self, colors, neededTime):
        total = 0
        i = 0
        n = len(colors)
        
        while i < n:
            j = i
            group_sum = 0
            group_max = 0
            
            # Traverse all consecutive balloons of the same color
            while j < n and colors[j] == colors[i]:
                group_sum += neededTime[j]
                group_max = max(group_max, neededTime[j])
                j += 1
            
            # Remove all except the max-time balloon
            total += group_sum - group_max
            
            i = j
        
        return total
