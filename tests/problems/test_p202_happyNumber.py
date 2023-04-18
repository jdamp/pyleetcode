from problems.p202_happy_number import is_happy, get_digit_square_sum
import pytest


@pytest.fixture
def happy_numbers() -> list[int]:
    return [7, 10, 13, 19, 23, 28, 31]


@pytest.fixture
def unhappy_numbers() -> list[int]:
    return [4, 8, 12, 25, 30]


def test_digit_square():
    assert get_digit_square_sum(1) == 1
    assert get_digit_square_sum(2) == 4
    assert get_digit_square_sum(25) == 29
    assert get_digit_square_sum(58) == 89


def test_happy_number(happy_numbers, unhappy_numbers):
    for n in happy_numbers:
        assert is_happy(n)
    for n in unhappy_numbers:
        assert not is_happy(n)
