def pairs(k, arr):
    # arr set for O(1) lookups
    arr_set = set(arr)
    # count of pairs
    count = 0
    # iterate through the array
    for num in arr:
        # check if num + k is in the set
        if num + k in arr_set:
            # increment count
            count += 1
    return count
