var solve = function(board) {
    const m = board.length;
    const n = board[0].length;

    // DFS to mark boundary-connected O's as safe
    function dfs(row, col) {
        // Out of bounds
        if (row < 0 || row >= m || col < 0 || col >= n) {
            return;
        }

        // Not an O
        if (board[row][col] !== 'O') {
            return;
        }

        // Mark as safe
        board[row][col] = '#';

        // Explore 4 directions
        dfs(row + 1, col);
        dfs(row - 1, col);
        dfs(row, col + 1);
        dfs(row, col - 1);
    }

    // 1. Process first and last column
    for (let row = 0; row < m; row++) {
        dfs(row, 0);
        dfs(row, n - 1);
    }

    // 2. Process first and last row
    for (let col = 0; col < n; col++) {
        dfs(0, col);
        dfs(m - 1, col);
    }

    // 3. Capture surrounded regions
    // 4. Restore safe regions
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (board[row][col] === 'O') {
                board[row][col] = 'X';
            } else if (board[row][col] === '#') {
                board[row][col] = 'O';
            }
        }
    }
};