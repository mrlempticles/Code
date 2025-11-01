from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            # Minimum potion required to achieve success
            min_required = (success + spell - 1) // spell  # ceiling division

            # Find the index of first valid potion
            idx = bisect_left(potions, min_required)

            # Count how many are successful
            res.append(m - idx)

        return res
