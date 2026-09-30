class Solution {
public:
    vector<vector<int>> result;
    vector<int> path;

    void dfs(TreeNode* node, int targetSum) {
        if (node == nullptr)
            return;

        path.push_back(node->val);
        targetSum -= node->val;

        // Check if this is a leaf
        if (node->left == nullptr && node->right == nullptr) {
            if (targetSum == 0) {
                result.push_back(path);
            }
        }

        // Explore children
        dfs(node->left, targetSum);
        dfs(node->right, targetSum);

        // Backtrack
        path.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        dfs(root, targetSum);
        return result;
    }
};