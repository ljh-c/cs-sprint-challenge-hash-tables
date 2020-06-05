def get_indices_of_item_weights(weights, length, limit):
    """
    Loop through weights
    - Store weight in dict as key and index as value
    - Item's partner has the weight (limit - weight of item)
    """
    items = {}

    for i, weight in enumerate(weights):
        weight_b = limit - weights[i]

        if weight_b not in items:
            items[weight] = i
        else:
            return (i, items[weight_b])

    return None
