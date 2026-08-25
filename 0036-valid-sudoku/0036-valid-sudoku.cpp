class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        // Check rows and columns
        for (int i = 0; i < 9; i++) {

            bool row[10] = {};
            bool col[10] = {};

            for (int j = 0; j < 9; j++) {

                // Check row
                if (board[i][j] != '.') {
                    int num = board[i][j] - '0';

                    if (row[num]) {
                        return false;
                    }

                    row[num] = true;
                }

                // Check column
                if (board[j][i] != '.') {
                    int num = board[j][i] - '0';

                    if (col[num]) {
                        return false;
                    }

                    col[num] = true;
                }
            }
        }

        // Check 3 x 3 boxes
        for (int row = 0; row < 9; row += 3) {
            for (int col = 0; col < 9; col += 3) {

                bool box[10] = {};

                for (int i = row; i < row + 3; i++) {
                    for (int j = col; j < col + 3; j++) {

                        if (board[i][j] != '.') {
                            int num = board[i][j] - '0';

                            if (box[num]) {
                                return false;
                            }

                            box[num] = true;
                        }
                    }
                }
            }
        }

        return true;
    }
};