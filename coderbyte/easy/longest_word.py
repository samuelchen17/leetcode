"""
Basically, I either use regex to make a new sentence without punctuation
or, iterate through the sentence, and remove punctuations

then loop through word in words, compare the length to longest word
or, return max(sentence.split(), key = len)
"""

import re


def LongestWordNew(sen):
    """
    Two methods,
    first method,
    use regex to remove punctuations
    then split the sentence into a list of words
    check the length of each word vs len longest word or
    just return max new list with key being length

    second method,
    iterate through the string
    if character is alpha or is numeric
    add word to new list
    if punctuation
    add space
    return max new list with key being length
    """

    # code goes here
    sen = re.sub(r"[^\w\s]", "", sen)

    return max(sen.split(), key=len)


# keep this function call here
print(LongestWordNew(input()))


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
