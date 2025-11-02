class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            # Exchange empty bottles for one full bottle
            empty -= numExchange
            numExchange += 1
            drunk += 1
            empty += 1  # drink the new bottle immediately

        return drunk
