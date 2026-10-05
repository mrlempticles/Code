class Solution {
public:
    int ans = 0;

    void solve(vector<int>& nums, int index, int currentXor) {
        // All elements processed
        if (index == nums.size()) {
            ans += currentXor;
            return;
        }

        // Don't include nums[index]
        solve(nums, index + 1, currentXor);

        // Include nums[index]
        solve(nums, index + 1, currentXor ^ nums[index]);
    }

    int subsetXORSum(vector<int>& nums) {
        solve(nums, 0, 0);
        return ans;
    }
};