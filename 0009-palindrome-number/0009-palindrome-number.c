#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    int reversed = 0;
    while (x > reversed) {
        reversed = reversed * 10 + x % 10;
        x = x / 10;
    }

    // For even and odd digit numbers
    return (x == reversed || x == reversed / 10);
}
