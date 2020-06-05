# Your code here



def finder(files, queries):
    """
    Hash each path: file as key and path as value
    """
    paths = {}
    result = []

    for path in files:
        name = path.split('/')[-1]

        if name not in paths:
            paths[name] = []

        paths[name].append(path)
    
    for query in queries:
        if query in paths:
            result.extend(paths[query])

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
