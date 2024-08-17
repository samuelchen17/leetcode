def is_palindrome(str):
    # initiate p1 and p2
    # p1 points at start of str
    # p2 points at end of str
    # compare p1 to p2
    # if same, p1++ p2--
    # if not, return false
    # if p1 == p2, return true

    p1, p2 = 0, len(str) - 1

    while p1 < p2:
        if str[p1] != str[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True


print(is_palindrome("hello"))  # false
print(is_palindrome("aba"))  # true
print(is_palindrome("abcba"))  # true
print(is_palindrome("abccba"))  # true
print(is_palindrome("melbourne"))  # false
print(is_palindrome("melbournem"))  # false
