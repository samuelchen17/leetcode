import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        make everything lowercase
        regex to remove all non alpha
        initiate p1 to start and p2 to len(s) - 1
        compare value at p1 and p2
        if value the same continue to loop
        if not, return False
        when p1 == p2 or p1 > p2, return true
        """
        lower = s.lower()
        lower = re.sub(r"[^a-z0-9]", "", lower)
        p1, p2 = 0, len(lower) - 1

        while p1 < p2:
            if lower[p1] != lower[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
