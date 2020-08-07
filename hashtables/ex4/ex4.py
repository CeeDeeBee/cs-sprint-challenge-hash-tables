def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # build hash table
    positives = a.copy()
    table = {}
    for num in a:
        if num < 0:
            positives.remove(num)
            table[num] = True

    result = []
    for num in positives:
        if table.get(num * -1):
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
