class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            
            if char not in count_s:
                count_s[char] = 1
            else:
                count_s[char] += 1

        for char in t:

            if char not in count_s:
                return False

            count_s[char] -= 1

            if count_s[char] < 0:
                return False
        
        return True

