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


def FirstReverseTwoPointer(strParam):
    """
    depends if to do in place or create new space
    in place:
    create p1 and p2
    if p1 == p2
      return the str
    elif
    """
    char_list = list(strParam)

    p1, p2 = 0, len(strParam) - 1
    while p1 < p2:
        char_list[p1], char_list[p2] = char_list[p2], char_list[p1]
        p1 += 1
        p2 -= 1

    return "".join(char_list)

    # code goes here
    return strParam


# keep this function call here
print(FirstReverseTwoPointer(input()))
