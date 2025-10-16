class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        res_signature = []

        for w in words:
            sig = ''.join(sorted(w))

            if res and res_signature[-1] == sig:
                continue 
            else:
                res.append(w)
                res_signature.append(sig)
        return res
