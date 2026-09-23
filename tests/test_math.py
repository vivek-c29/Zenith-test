from buggy_math import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, -5) == -10
    assert add_numbers('2', '3') == 5
    assert add_numbers('10', 5) == 15
    assert add_numbers(5, '10') == 15
    try:
        add_numbers('a', 1)
    except ValueError:
        pass  # Expected ValueError
    try:
        add_numbers(1, 'b')
    except ValueError:
        pass  # Expected ValueError
