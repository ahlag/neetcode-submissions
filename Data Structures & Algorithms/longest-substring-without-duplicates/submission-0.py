class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            print('r:', r)
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            print('charSet:', charSet)
            res = max(res, r - l + 1)
            print('res:', res)

        return res
        