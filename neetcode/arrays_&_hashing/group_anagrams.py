from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create hashmap key = sorted characters, value = word
        loop through the array
        sort the word in alpha
        check if sorted word in hashmap
        if yes, append the word
        if not, create a new key and save word
        after going through all strings
        return all the lists from the hashmap
        """

        str_map = {}

        for word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if sorted_word in str_map:
                str_map[sorted_word].append(word)
            else:
                str_map[sorted_word] = [word]

        # can just return the values of the hashmap
        return list(str_map.values())
