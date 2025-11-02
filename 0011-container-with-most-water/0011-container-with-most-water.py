class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # calculate the area between the two lines
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            if area > max_area:
                max_area = area

            # move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
