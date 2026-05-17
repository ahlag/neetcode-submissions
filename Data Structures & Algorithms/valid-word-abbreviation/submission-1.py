class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i, j = 0, 0
        w = len(word)
        a = len(abbr)

        while i < w and j < a:

            digit_str = ''

            if word[i] != abbr[j]:

                if not abbr[j].isdigit() or abbr[j] == '0':
                    return False
                else:
                    while  j < a and abbr[j].isdigit():
                        digit_str += abbr[j]
                        j += 1
                
            if len(digit_str) != 0:
                digit = int(digit_str)
                for _ in range(digit):
                    i += 1
            else:
                i += 1
                j += 1


        return i == w and j == a

        