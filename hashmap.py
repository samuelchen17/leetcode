from collections import defaultdict


def number_of_unique_names(names):
    """
    inputs:
    names - array of strings
    output:
    number of unique names in array
    """

    # create hashmap, initiate count
    # iterate through names
    # when name is found, create key in hashmap
    # count++
    # go next name
    # check if name exists in key
    # if key exists, count does not change
    # if not, add new key to hashmap, count++
    # continue until end of names
    # return count

    # use hashmap
    names_map = {}
    count = 0

    for name in names:
        if not names_map.get(name):
            names_map[name] = name
            count += 1

    return count


list = ["roy", "roy", "roy", "sam", "fran", "abi", "abi"]  # 4 names

print(number_of_unique_names(list))
