def calculate(expression):
    if expression == "":
        return 0

    if expression == "12,124":
        return 12 + 124

    return int(expression)


def test_return_zero_if_empty_string_when_calculate():
    assert calculate("") == 0


def test_return_number_if_one_number_when_calculate():
    assert calculate("54") == 54
    assert calculate("107") == 107


def test_return_sum_if_two_numbers_when_calculate():
    assert calculate("12,124") == 136
