def func_executor(*args):
    result = []
    for func, data in args:
        result.append(f"{func.__name__} - {func(*data)}")

    return "\n".join(result)