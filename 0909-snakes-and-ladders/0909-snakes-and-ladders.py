from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        target = n * n

        def get_position(square):
            r = (square - 1) // n
            c = (square - 1) % n

            row = n - 1 - r

            if r % 2 == 1:
                col = n - 1 - c
            else:
                col = c

            return row, col

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            square, moves = queue.popleft()

            if square == target:
                return moves

            for next_square in range(square + 1, min(square + 6, target) + 1):
                row, col = get_position(next_square)

                if board[row][col] != -1:
                    next_square = board[row][col]

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1