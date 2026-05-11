class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        right = 0
        left = 0
        best_len = 0
        for right in range(0, len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best_len = max(best_len, right - left + 1)
        return best_len
