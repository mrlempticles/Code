class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pos = [-1]
        for i, ch in enumerate(s):
            if ch == '0':
                pos.append(i)
        pos.append(n)

        m = len(pos) - 2  # number of zeros
        ans = 0
        LIM = int(n**0.5) + 2

       
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1

        
        for z in range(1, LIM):
            if z > m:
                break
            S = z * z + z  # required minimal length = ones+zeros = z^2 + z
           
            for i_zero in range(1, m - z + 2):
                leftChoices = pos[i_zero] - pos[i_zero - 1]        # possible starts count
                rightChoices = pos[i_zero + z] - pos[i_zero + z - 1]  # possible ends count
                baseLen = pos[i_zero + z - 1] - pos[i_zero] + 1

                need = S - baseLen
                if need <= 0:
                    # every pair (a,b) is valid
                    ans += leftChoices * rightChoices
                    continue

                
                totalPairs = leftChoices * rightChoices

                
                k = need - 1

                
                if k >= leftChoices + rightChoices - 2:
                    bad = totalPairs
                else:
                    
                    A = leftChoices
                    B = rightChoices
                    max_a = min(A - 1, k)
                    if max_a < 0:
                        bad = 0
                    else:
                        
                        t = k - B + 1
                        full_count_end = min(max_a, t)  # a in [0..full_count_end] have min=B
                        bad = 0
                        if full_count_end >= 0:
                            bad += (full_count_end + 1) * B
                        \
                        u = max(t + 1, 0)
                        if u <= max_a:
                            \
                            low = k - max_a + 1
                            high = k - u + 1
                            cnt = (high - low + 1)
                            bad += (low + high) * cnt // 2

                valid = totalPairs - bad
                if valid > 0:
                    ans += valid

        return ans
