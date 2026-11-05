
class Solution(object):
    def findAnagrams(self, s, p):
        result = []

        if len(p) > len(s):
            return result

        pCount = [0] * 26
        sCount = [0] * 26

        for i in range(len(p)):
            pCount[ord(p[i]) - ord('a')] += 1
            sCount[ord(s[i]) - ord('a')] += 1

        if pCount == sCount:
            result.append(0)

        left = 0

        for right in range(len(p), len(s)):

            sCount[ord(s[right]) - ord('a')] += 1

            sCount[ord(s[left]) - ord('a')] -= 1

            left += 1

            if sCount == pCount:
                result.append(left)

        return result
