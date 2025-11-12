import pytest

from assignment import (
    square,
    triange1,
    triangle2,
    triangle3,
    find_first_digit,
    loop_over_all_digits,
    luhn_check,
)

# Helper to normalize line endings
def normalize(s: str) -> str:
    return s.replace("\r\n", "\n")

@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "#\n"),
        (2, "##\n##\n"),
        (5, "#####\n#####\n#####\n#####\n#####\n"),
    ],
)
def test_square_prints(n, expected, capsys):
    square(n)
    captured = capsys.readouterr()
    assert normalize(captured.out) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "#\n"),
        (3, "#\n##\n###\n"),
        (5, "#\n##\n###\n####\n#####\n"),
    ],
)
def test_triange1_prints(n, expected, capsys):
    triange1(n)
    captured = capsys.readouterr()
    assert normalize(captured.out) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "#\n"),
        (3, "###\n##\n#\n"),
        (5, "#####\n####\n###\n##\n#\n"),
    ],
)
def test_triangle2_prints(n, expected, capsys):
    triangle2(n)
    captured = capsys.readouterr()
    assert normalize(captured.out) == expected


@pytest.mark.parametrize("n", [1, 3, 5])
def test_triangle3_prints_centered(n, capsys):
    triangle3(n)
    captured = capsys.readouterr()
    expected = "".join((" " * (n - i) + "#" * (2 * i - 1) + "\n") for i in range(1, n + 1))
    assert normalize(captured.out) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (12345, 1),
        (9081726354, 9),
        (0, 0),
        (-567, 5),
        (100000, 1),
    ],
)
def test_find_first_digit(value, expected):
    assert find_first_digit(value) == expected


@pytest.mark.parametrize(
    "value,expected_output",
    [
        (123, "1\n2\n3\n"),
        (9081726354, "9\n0\n8\n1\n7\n2\n6\n3\n5\n4\n"),
        (0, "0\n"),
        (-204, "2\n0\n4\n"),
    ],
)
def test_loop_over_all_digits_prints(value, expected_output, capsys):
    loop_over_all_digits(value)
    captured = capsys.readouterr()
    assert normalize(captured.out) == expected_output


@pytest.mark.parametrize(
    "value,expected",
    [
        (49927398716, True),
        (1234567812345670, True),
        (1234567812345678, False),
        (0, False),  # 0 is not a valid Luhn-valid multi-digit number
        (79927398713, True),  # common Luhn example
        (79927398710, False),
    ],
)
def test_luhn_check(value, expected):
    assert luhn_check(value) is expected
