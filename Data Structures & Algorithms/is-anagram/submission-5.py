class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m, n = len(s), len(t)

        if m != n:
            return False

        countS, countT = {}, {}

        for i in range(m):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT


        