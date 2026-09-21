import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.pos:
            return False

        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1

        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val not in self.pos:
            return False

        index = self.pos[val]
        last = self.nums[-1]

        # Move the last element into the position
        # of the element we want to remove
        self.nums[index] = last
        self.pos[last] = index

        # Remove the last element
        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.nums)