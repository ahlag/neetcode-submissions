class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # A string starting with '0' is invalid
        if s[0] == '0':
            return 0

        # dp[i] = number of ways to decode the first i characters
        # dp[0] = 1 means the empty string has one valid way
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1  # first character is already confirmed not '0'

        # Build the answer from left to right
        for i in range(2, n + 1):
            # Last one digit
            one = s[i - 1]

            # Last two digits
            two = s[i - 2:i]

            # If one digit is valid ('1' to '9'),
            # then we can extend all decodings up to i-1
            if one != '0':
                dp[i] += dp[i - 1]

            # If two digits form a valid letter ('10' to '26'),
            # then we can extend all decodings up to i-2
            if 10 <= int(two) <= 26:
                dp[i] += dp[i - 2]

        # Number of ways to decode the whole string
        return dp[n]