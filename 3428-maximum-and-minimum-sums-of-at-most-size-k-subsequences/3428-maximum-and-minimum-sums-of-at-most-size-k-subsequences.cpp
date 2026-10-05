class Solution {
public:
    static const long long MOD = 1000000007;

    int minMaxSums(vector<int>& nums, int k) {
        int n = nums.size();

        sort(nums.begin(), nums.end());

        // C[n][r]
        vector<vector<long long>> C(n + 1, vector<long long>(k, 0));

        C[0][0] = 1;

        for (int i = 1; i <= n; i++) {
            C[i][0] = 1;

            for (int j = 1; j < k; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }

        long long ans = 0;

        for (int i = 0; i < n; i++) {

            // nums[i] is the minimum
            long long minWays = 0;

            for (int j = 0; j < k; j++) {
                if (i + j < n)
                    minWays = (minWays + C[n - i - 1][j]) % MOD;
            }

            // nums[i] is the maximum
            long long maxWays = 0;

            for (int j = 0; j < k; j++) {
                if (j <= i)
                    maxWays = (maxWays + C[i][j]) % MOD;
            }

            ans = (ans + nums[i] * ((minWays + maxWays) % MOD)) % MOD;
        }

        return ans;
    }
};