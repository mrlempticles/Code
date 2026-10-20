
class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        longest = 0
        i = 1

        while i < n - 1:
            # Find a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i
                right = i

                # Expand left while increasing
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Expand right while decreasing
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                longest = max(longest, right - left + 1)
                i = right
            else:
                i += 1

        return longest
