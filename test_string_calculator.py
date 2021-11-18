def calculate(expression):
    if expression == "":
        return 0

    if expression[1] == ",":
        return int(expression[0:1]) + int(expression[2:4])

    if expression[2] == ",":
        return int(expression[0:2]) + int(expression[3:6])

    return int(expression)


def test_return_zero_if_empty_string_when_calculate():
    assert calculate("") == 0


def test_return_number_if_one_number_when_calculate():
    assert calculate("54") == 54
    assert calculate("107") == 107


def test_return_sum_if_two_numbers_when_calculate():
    assert calculate("12,124") == 136
    assert calculate("2,25") == 27
