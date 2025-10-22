class Solution:
    def maxFreqSum(self, s):
        vowels = "aeiouAEIOU"
        vowel_count = {}
        consonant_count = {}

        for ch in s:
            if ch.isalpha():
                if ch.lower() in "aeiou":
                    vowel_count[ch.lower()] = vowel_count.get(ch.lower(), 0) + 1
                else:
                    consonant_count[ch.lower()] = consonant_count.get(ch.lower(), 0) + 1

        # Get max frequency for vowels
        max_vowel_freq = max(vowel_count.values()) if vowel_count else 0

        # Get max frequency for consonants
        max_consonant_freq = max(consonant_count.values()) if consonant_count else 0

        # Return the sum
        return max_vowel_freq + max_consonant_freq
