var longestConsecutive = function(nums) {
    const set = new Set(nums);
    let longest = 0;

    for (const num of set) {
        // Only start counting if num is the beginning
        // of a consecutive sequence
        if (!set.has(num - 1)) {
            let current = num;
            let length = 1;

            while (set.has(current + 1)) {
                current++;
                length++;
            }

            longest = Math.max(longest, length);
        }
    }

    return longest;
};