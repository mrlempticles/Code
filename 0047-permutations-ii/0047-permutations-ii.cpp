class Solution {
public:

    vector<vector<int>> ans;

    void backtrack(vector<int>& nums,
                   vector<int>& current,
                   vector<bool>& used) {

        // Complete permutation
        if (current.size() == nums.size()) {
            ans.push_back(current);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {

            // Already used in current permutation
            if (used[i]) {
                continue;
            }

            // Skip duplicate choices at the same level
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }

            // Choose
            current.push_back(nums[i]);
            used[i] = true;

            // Explore
            backtrack(nums, current, used);

            // Undo
            current.pop_back();
            used[i] = false;
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {

        // Put duplicates next to each other
        sort(nums.begin(), nums.end());

        vector<int> current;
        vector<bool> used(nums.size(), false);

        backtrack(nums, current, used);

        return ans;
    }
};