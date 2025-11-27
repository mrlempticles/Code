class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        count = 0

        for ch in s:
            if ch == '1':
                count += 1
            else:
                ans = (ans + count * (count + 1) // 2) % MOD
                count = 0

        # Add last group if string ends with '1'
        ans = (ans + count * (count + 1) // 2) % MOD

        return ans
