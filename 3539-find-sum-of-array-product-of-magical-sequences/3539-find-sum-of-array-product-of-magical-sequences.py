MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m, k, nums):
        n = len(nums)

        # Precompute factorials and inverse factorials
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        # Precompute nums[i]^f
        pow_nums = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for f in range(1, m + 1):
                pow_nums[i][f] = pow_nums[i][f - 1] * nums[i] % MOD

        # Precompute multipliers nums[i]^f * invfact[f]
        mult = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for f in range(m + 1):
                mult[i][f] = pow_nums[i][f] * invfact[f] % MOD

        # DP dict: (used, carry, ones) -> accumulated sum contribution
        dp = {(0, 0, 0): 1}

        for i in range(n):
            newdp = {}
            for (used, carry, ones), val in dp.items():
                maxf = m - used
                for f in range(maxf + 1):
                    new_used = used + f
                    total = carry + f

                    bit = total & 1
                    new_ones = ones + bit
                    if new_ones > k:
                        continue

                    new_carry = total >> 1

                    add = val * mult[i][f] % MOD
                    key = (new_used, new_carry, new_ones)
                    newdp[key] = (newdp.get(key, 0) + add) % MOD

            dp = newdp

        # Final collect: must use exactly m items, and total 1-bits = k
        ans = 0
        for (used, carry, ones), val in dp.items():
            if used == m:
                # portable popcount
                if ones + bin(carry).count("1") == k:
                    ans = (ans + val) % MOD

        return ans * fact[m] % MOD
