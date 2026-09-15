class Solution {
public:

    Node* solve(vector<vector<int>>& grid, int r, int c, int size) {

        // Check if the current square has the same value
        bool same = true;
        int value = grid[r][c];

        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                if (grid[i][j] != value) {
                    same = false;
                    break;
                }
            }
            if (!same) break;
        }

        // If all values are same, create a leaf node
        if (same) {
            return new Node(value, true);
        }

        // Divide the grid into 4 parts
        int half = size / 2;

        Node* topLeft = solve(grid, r, c, half);
        Node* topRight = solve(grid, r, c + half, half);
        Node* bottomLeft = solve(grid, r + half, c, half);
        Node* bottomRight = solve(grid, r + half, c + half, half);

        // Current node is not a leaf
        return new Node(0, false, topLeft, topRight,
                        bottomLeft, bottomRight);
    }

    Node* construct(vector<vector<int>>& grid) {
        int n = grid.size();

        return solve(grid, 0, 0, n);
    }
};