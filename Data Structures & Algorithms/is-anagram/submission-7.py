class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m, n = len(s), len(t)

        if m != n:
            return False

        count = [0] * 26

        for i in range(m):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
            
        return True


        