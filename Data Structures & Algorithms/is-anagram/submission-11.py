class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countT, countS = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countT[t[i]] = countT.get(t[i], 0) + 1
            countS[s[i]] = countS.get(s[i], 0) + 1

        return countT == countS
        