class Solution {
public:

    vector<vector<int>> ans;

    void backtrack(vector<int>& candidates,
                   int target,
                   int start,
                   vector<int>& current) {

        // Target achieved
        if (target == 0) {
            ans.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {

            // Skip duplicate values at the same level
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }

            // Since array is sorted, no later value can work
            if (candidates[i] > target) {
                break;
            }

            // Choose
            current.push_back(candidates[i]);

            // i + 1 because each element can only be used once
            backtrack(candidates,
                      target - candidates[i],
                      i + 1,
                      current);

            // Undo choice
            current.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates,
                                         int target) {

        // Sorting helps with duplicate removal
        // and early stopping
        sort(candidates.begin(), candidates.end());

        vector<int> current;

        backtrack(candidates, target, 0, current);

        return ans;
    }
};