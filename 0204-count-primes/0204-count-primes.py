class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = bytearray(b'\x01') * n
        is_prime[0] = 0
        is_prime[1] = 0

        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                start = p * p
                is_prime[start:n:p] = b'\x00' * (((n - 1 - start) // p) + 1)

        return sum(is_prime)