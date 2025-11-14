class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = [int(c) for c in s]

        while len(arr) > 2:
            nxt = []
            for i in range(len(arr) - 1):
                nxt.append((arr[i] + arr[i+1]) % 10)
            arr = nxt

        return arr[0] == arr[1]