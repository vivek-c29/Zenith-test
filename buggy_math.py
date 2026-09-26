def add_numbers(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError('Both inputs must be convertible to integers.')
    return a * b
