import re


def UsernameValidation(strParam):

    if len(strParam) < 4 or len(strParam) > 25:
        return False
    elif strParam[0].isalpha() != True:
        return False
    elif strParam[-1] == "_":
        return False

    if not re.match("^[A-Za-z0-9_]+$", strParam):
        return False

    # code goes here
    return True


# keep this function call here
print(UsernameValidation(input()))
