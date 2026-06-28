class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_set = {}
        t_set = {}

        for i in range(len(s)):
            s_set[s[i]] = 0 if s[i] not in s_set else s_set[s[i]] + 1
            t_set[t[i]] = 0 if t[i] not in t_set else t_set[t[i]] + 1

        return s_set == t_set