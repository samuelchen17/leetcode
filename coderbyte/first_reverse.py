def FirstReverse(strParam):
    """
    find length of the str
    set pointer to the end
    iterate from the end while adding the characters to a new array
    return the new array
    """
    reverse = []
    p = len(strParam) - 1
    while p > -1:
        reverse.append(strParam[p])
        p -= 1

    # convert array to string
    return "".join(reverse)


# keep this function call here
print(FirstReverse(input()))
