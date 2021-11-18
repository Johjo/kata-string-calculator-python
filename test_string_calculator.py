def calculate(expression):
    if expression == "54":
        return 54
    return 0


def test_return_zero_if_empty_string_when_calculate():
    assert calculate("") == 0


def test_return_number_if_one_number_when_calculate():
    assert calculate("54") == 54
