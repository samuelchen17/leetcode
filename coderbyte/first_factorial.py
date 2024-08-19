def fact(num):
    # base case
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


def FirstFactorial(num):
    """
    recursively solve this
    """

    # base case
    if num == 0:
        return 1

    return num * FirstFactorial(num - 1)
