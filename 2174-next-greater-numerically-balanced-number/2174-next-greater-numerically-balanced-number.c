#include <stdbool.h>

bool isBalanced(int x) {
    int cnt[10] = {0};
    int y = x;

    while (y > 0) {
        int d = y % 10;
        if (d == 0)
            return false;
        cnt[d]++;
        y /= 10;
    }

    for (int d = 1; d <= 9; d++) {
        if (cnt[d] != 0 && cnt[d] != d)
            return false;
    }

    return true;
}

int nextBeautifulNumber(int n) {   // ✅ correct name for LeetCode
    int x = n + 1;
    while (true) {
        if (isBalanced(x))
            return x;
        x++;
    }
}
