
class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        answer = []

        for i in range(1, n - k):
            answer.append(i)

        left, right = n - k, n

        while left <= right:
            answer.append(left)
            left += 1

            if left <= right:
                answer.append(right)
                right -= 1

        return answer