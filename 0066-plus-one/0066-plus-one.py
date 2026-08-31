class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9,
            # simply add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0
            # and carry 1 to the next digit
            digits[i] = 0

        # If we reach here, every digit was 9
        return [1] + digits