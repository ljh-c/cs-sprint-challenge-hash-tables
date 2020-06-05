def has_negatives(a):
    """
    Hash each number: number as key and counterpart as value
    """
    seen = {}
    result = []

    for num in a:
        if -num in seen:
            result.append(abs(num))
        else:
            seen[num] = None

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
