class Solution:
    def countPalindromicSubsequence(self, s):
        # record first and last index of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0
        # for each character that can be both ends (first < last)
        for ch in first:
            if first[ch] < last[ch]:
                seen = set()
                # collect distinct middle characters between first and last
                for j in range(first[ch] + 1, last[ch]):
                    seen.add(s[j])
                ans += len(seen)

        return ans