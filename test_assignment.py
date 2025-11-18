import pytest

from assignment import find_first_digit, loop_over_all_digits, luhn_check

def test_find_first_digit():
    assert find_first_digit(12345) == 1
    assert find_first_digit(9081726354) == 9
    assert find_first_digit(-456) == 4
    assert find_first_digit(0) == 0
    assert find_first_digit(-0) == 0
    assert find_first_digit(3.14159) == 3
    assert find_first_digit(-2.71828) == 2
    assert find_first_digit("abc") is None

def test_loop_over_all_digits():
    assert loop_over_all_digits(123) == [1, 2, 3]
    assert loop_over_all_digits(9081726354) == [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    assert loop_over_all_digits(-456) == [4, 5, 6]
    assert loop_over_all_digits(0) == [0]
    assert loop_over_all_digits(3.14159) == [3, 1, 4, 1, 5, 9]
    assert loop_over_all_digits(-2.71828) == [2, 7, 1, 8, 2, 8]

def test_luhn_check():
    assert luhn_check(49927398716) is True
    assert luhn_check(1234567812345670) is True
    assert luhn_check(1234567812345678) is False
    assert luhn_check(79927398713) is True
    assert luhn_check(79927398714) is False
    assert luhn_check(0) is True
    assert luhn_check(1) is False
