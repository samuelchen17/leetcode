def QuestionsMarksNew(strParam):
    """
    create hashmap
    iterate through string
    if number
      difference = 10 - number
      if difference in hashmap
        grab the array beginning from hashmap index to current index
        loop through to count question marks
        if at end
        if count != 3
          return False
        else:
          pairfound = true
      save to hashmap
      key = value, value = index
    Return pairfound
    """
    hashmap = {}
    pair_found = False

    for i, char in enumerate(strParam):
        if char.isnumeric():
            num = int(char)
            difference = 10 - num
            if difference in hashmap:
                count = 0
                subStr = strParam[hashmap[difference] : i]
                for char in subStr:
                    if char == "?":
                        count += 1
                if count != 3:
                    return False
                else:
                    pair_found = True
            hashmap[num] = i
    return pair_found


# keep this function call here
print(QuestionsMarksNew(input()))


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
