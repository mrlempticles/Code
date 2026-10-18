
class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    top = stack.pop()
                    result = abs(top) // abs(num)
                    if top * num < 0:
                        result = -result
                    stack.append(result)

                sign = char
                num = 0

        return sum(stack)
