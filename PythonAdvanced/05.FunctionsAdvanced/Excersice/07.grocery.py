def grocery_store(**kwargs):
    receipt = sorted(kwargs.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
    result = []
    for product, quantity in receipt:
        result.append(f"{product}: {quantity}")
    return "\n".join(result)