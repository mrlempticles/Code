int abs_int(int x) {
    return x < 0 ? -x : x;
}

int countValidSelections(int* nums, int n) {
    int S = 0;
    for (int i = 0; i < n; i++)
        S += nums[i];
    int valid = 0, L = 0;

    for (int i = 0; i < n; i++) {
        if (nums[i] != 0)
            L += nums[i];
        else {
            int R = S - L;
            if (L == R)
                valid += 2;
            else if (abs_int(L - R) == 1)
                valid += 1;
        }
    }
    return valid;
}
