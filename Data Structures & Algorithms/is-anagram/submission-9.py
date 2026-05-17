class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = {}

        n, m = len(s), len(t)

        if n != m:
            return False

        for i in range(n):
            if ord(s[i]) - ord('a') not in count:
                count[ord(s[i]) - ord('a')] = 1
            else:
                count[ord(s[i]) - ord('a')] += 1

        for j in range(m):
            if ord(t[j]) - ord('a') not in count:
                return False
            count[ord(t[j]) - ord('a')] -= 1
            if count[ord(t[j]) - ord('a')] < 0:
                return False

        return True
            
        