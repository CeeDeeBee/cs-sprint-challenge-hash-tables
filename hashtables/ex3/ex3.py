def intersection(arrays):
    """
    YOUR CODE HERE
    """
    list_nums = {}
    # initialize dict with first array
    for num in arrays[0]:
        list_nums[num] = 0

    for i in range(1, len(arrays)):
        for num in arrays[i]:
            if num in list_nums:
                if list_nums[num] == i - 1:  # if num was in last array
                    list_nums[num] = i
                else:
                    del list_nums[num]

    result = []
    for item in list_nums.items():
        if item[1] == len(arrays) - 1:
            result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
