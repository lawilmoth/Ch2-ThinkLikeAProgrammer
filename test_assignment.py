import pytest
import sys

from assignment import (
    draw_square,
    triange1,
    triangle2,
    triangle3,
    find_first_digit,
    loop_over_all_digits,
    luhn_check,
)

def test_draw_square(capsys):

    draw_square(3)
    captured = capsys.readouterr()
    assert captured.out == "###\n###\n###\n"

    draw_square(5)
    captured = capsys.readouterr()
    assert captured.out == "#####\n#####\n#####\n#####\n#####\n"
def test_triange1(capsys):
    triange1(3)
    captured = capsys.readouterr()
    assert captured.out == "#\n##\n###\n"

    triange1(5)
    captured = capsys.readouterr()
    assert captured.out == "#\n##\n###\n####\n#####\n"


def test_triangle2(capsys):
    triangle2(3)
    captured = capsys.readouterr()
    assert captured.out == "###\n##\n#\n"

    triangle2(5)
    captured = capsys.readouterr()
    assert captured.out == "#####\n####\n###\n##\n#\n"


def test_triangle3(capsys):
    triangle3(3)
    captured = capsys.readouterr()
    assert captured.out == "  #\n ###\n#####\n"

    triangle3(5)
    captured = capsys.readouterr()
    assert captured.out == "    #\n   ###\n  #####\n #######\n#########\n"


def test_find_first_digit():
    assert find_first_digit(12345) == 1
    assert find_first_digit(9081726354) == 9


def test_loop_over_all_digits(capsys):
    loop_over_all_digits(123)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n"

    loop_over_all_digits(9081726354)
    captured = capsys.readouterr()
    assert captured.out == "9\n0\n8\n1\n7\n2\n6\n3\n5\n4\n"


def test_luhn_check():
    assert luhn_check(49927398716) is True
    assert luhn_check(1234567812345670) is True
    assert luhn_check(1234567812345678) is False


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
