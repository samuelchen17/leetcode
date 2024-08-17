class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        first, check if both strings are equal length
        create hashmap, loop through first array
        store char as key, count as value
        loop through second array, check if char exists in hashmap
        if it does exist, remove one from count
        if it doesnt return false
        when count reaches 0, remove key value pair
        at the end, check if hashmap is empty
        if empty return true
        if not return false
        """

        # check if strings are equal
        if len(s) != len(t):
            return False

        char_map = {}

        # go through first array
        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1

        # go through second array
        for char in t:
            if char in char_map:
                # remove count
                char_map[char] -= 1
                # nest this if statement, only needs to run when decrement
                if char_map[char] == 0:
                    # delete count
                    del char_map[char]
            else:
                return False

        # check if hashmap is empty
        # if empty return true else return false
        if len(char_map) == 0:
            return True
        else:
            return False
