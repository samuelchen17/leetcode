# The list option is better in this case for its simplicity and space usage for the problem


def FindIntersection(strArr):
    """
    since it is already sorted, we can leverage that.
    create two pointers, pointing at the start of strArr[0] and strArr[1]
    create a loop where, pointer 1 will increment until the index is the same as pointer 2
    when p1 and p2 are the same, p2 will increase by 1
    at any point if the value of pointer 1 exceeds that of pointer 2, pointer 2 will increase
    if the value of p1 = p2, append to a variable
    when either of the pointers reach the end of the list, return the variable and add the commas back in
    """

    # split string into array of int
    list1 = list(map(int, strArr[0].split(",")))
    list2 = list(map(int, strArr[1].split(",")))

    # initialize pointers
    p1, p2 = 0, 0

    # initialize result list
    intersection = []

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            p1 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            intersection.append(list1[p1])
            p1 += 1
            p2 += 1

    if intersection:
        return ",".join(map(str, intersection))
    else:
        return "false"


# keep this function call here
print(FindIntersection(input()))


def FindIntersectionHash(strArr):
    """
    leverage the sorted arrays
    convert both elements to list of int
    create two pointers
    create hashmap to store intersection
    loop through the array
    if value of arr[p1] == arr[p2]
      store in hashmap
      p1++, p2++
    if value of arr[p1] > arr[p2]
      p2++
    elif value of arr[p2] > arr[p1]
      p1++
    return list hashmap keys, if empty return false
    """

    list1 = list(map(int, strArr[0].split(",")))
    list2 = list(map(int, strArr[1].split(",")))

    p1, p2 = 0, 0
    intersection = {}

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            intersection[list1[p1]] = 0
            p1 += 1
            p2 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1

    if intersection:
        return list(intersection.keys())
    else:
        return False

    # code goes here
    return strArr


# keep this function call here
print(FindIntersectionHash(input()))
