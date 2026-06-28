class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for word in strs:
            charSet = [0] * 26
            for c in word:
                charSet[ord('a') - ord(c)] += 1
            res[str(charSet)].append(word)

        return list(res.values())