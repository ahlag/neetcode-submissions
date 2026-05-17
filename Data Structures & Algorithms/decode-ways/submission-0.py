class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev2 = 1  # ways to decode empty string
        prev1 = 1  # ways to decode first char

        for i in range(1, len(s)):
            curr = 0

            # take one digit
            if s[i] != '0':
                curr += prev1

            # take two digits
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1