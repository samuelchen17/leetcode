def QuestionsMarks(strParam):
    """
    use hashmap to store the number as key and index as value
    while loop to loop through the str
    check for difference, difference = 10 - number
    check if difference is in hashmap
    if it is, grab its index and the current index
    loop through that sub array to count number of ?
    if not equal to 3, return false
    continue until end of list
    """

    number_map = {}
    found_pair = False

    for i, char in enumerate(strParam):
        # check if it is a number
        if char.isdigit():
            num = int(char)
            difference = 10 - num
            # if the difference exists in hashmap
            if difference in number_map:
                count = 0
                # make a substring
                subStr = strParam[number_map[difference] : i]
                # loop through the characters in substring
                for c in subStr:
                    if c == "?":
                        count += 1
                if count != 3:
                    return "false"
                found_pair = True
            # add to map
            number_map[num] = i

    return "true" if found_pair else "false"


# keep this function call here
print(QuestionsMarks(input()))
