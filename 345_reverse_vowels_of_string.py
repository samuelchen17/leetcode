class Solution:
    def reverseVowels(self, s: str) -> str:
        # pointer from start keeps going till points to first vowel
        # then pointer from end finds first vowel
        # switch positions
        # keep going while starter pointer is less than end pointer
        l = list(s)
        p1, p2 = 0, len(s) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while p1 < p2:
            if s[p1] not in vowels:
                p1 += 1
                continue
            if s[p2] not in vowels:
                p2 -= 1
                continue

            l[p1], l[p2] = l[p2], l[p1]
            p1 += 1
            p2 -= 1
        return "".join(l)
