class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        vector<int> arr = nums;
        sort(arr.begin(), arr.end());

        int n = nums.size();
        int mid = (n + 1) / 2;

        int left = mid - 1;
        int right = n - 1;

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = arr[left--];
            } else {
                nums[i] = arr[right--];
            }
        }
    }
};