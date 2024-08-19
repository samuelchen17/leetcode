import re


def CodelandUsernameValidation(strParam):
    """
    check if first is a letter
    check if last is a underscore
    check if letters, numbers and underscore
    """

    s = strParam

    if s[-1] == "_":
        return False
    if s[0].isalpha() != True:
        return False
    if len(s) < 4 or len(s) > 25:
        return False

    if not re.match("^[A-Za-z0-9_]+$", s):
        return False

    return True

    # code goes here
    return strParam


# keep this function call here
print(CodelandUsernameValidation(input()))
