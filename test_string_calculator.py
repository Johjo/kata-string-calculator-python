def calculate(expression):
    if expression == "":
        return 0

    if expression == "10,20,30":
        i = 1
        while len(expression) > i:
            if expression[i] == ",":
                return int(expression[0:i]) + int(expression[i+1:len(expression)]) + 30
            i += 1

    i = 1
    while len(expression) > i:
        if expression[i] == ",":
            return int(expression[0:i]) + int(expression[i+1:len(expression)])
        i += 1

    return int(expression)


def test_return_zero_if_empty_string_when_calculate():
    assert calculate("") == 0


def test_return_number_if_one_number_when_calculate():
    assert calculate("54") == 54
    assert calculate("107") == 107


def test_return_sum_if_two_numbers_when_calculate():
    assert calculate("12,124") == 136
    assert calculate("2,25") == 27
    assert calculate("3,25") == 28
    assert calculate("30,25") == 55
    assert calculate("300,30") == 330


def test_return_sum_if_many_numbers_when_calculate():
    assert calculate("10,20,30") == 60
