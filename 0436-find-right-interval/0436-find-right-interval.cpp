class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {

        int n = intervals.size();

        // Store {start, original index}
        vector<pair<int, int>> starts;

        for (int i = 0; i < n; i++) {
            starts.push_back({intervals[i][0], i});
        }

        // Sort by start
        sort(starts.begin(), starts.end());

        vector<int> ans(n, -1);

        for (int i = 0; i < n; i++) {

            int end = intervals[i][1];

            // Binary search for first start >= end
            int left = 0;
            int right = n - 1;
            int index = -1;

            while (left <= right) {

                int mid = left + (right - left) / 2;

                if (starts[mid].first >= end) {
                    // This can be our answer
                    index = starts[mid].second;

                    // Try to find an even smaller start
                    right = mid - 1;
                }
                else {
                    // Start is too small
                    left = mid + 1;
                }
            }

            ans[i] = index;
        }

        return ans;
    }
};