# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # initialize queries hash table
    query_table = {}
    for query in queries:
        query_table[query] = True

    result = []
    for f in files:
        if query_table.get(f.split("/")[-1]):
            result.append(f)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
