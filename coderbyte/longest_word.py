import re


def LongestWord(sen):
    """
    first use regex to remove all punctuation
    then split the sentence into words
    create a largest_word variable
    for word in words
    check if length of word is greater than largest word
    if greater, make largest word = word
    return largest word
    """

    # remove punctuation with regex
    sen = re.sub(r"[^\w\s]", "", sen)

    # split the sentence into words
    words = sen.split()

    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
