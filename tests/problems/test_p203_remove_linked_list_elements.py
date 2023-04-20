import pytest

from data_structures import LinkedList
from problems.p203_remove_linked_list_elements import remove_elements

@pytest.fixture
def leetcode_examples():
    inputs = [
        [1, 2, 6, 3, 4, 5, 6],
        [],
        [7, 7, 7, 7]
    ]
    vals = [6, 1, 7]
    outputs = [
        [1, 2, 3, 4, 5],
        [],
        []
    ]
    return zip(inputs, vals, outputs)


def test_remove_elements(leetcode_examples):
    for inp, val, out in leetcode_examples:
        linked_list = LinkedList.from_value_list(inp)
        assert remove_elements(linked_list, val).to_value_list() == out
