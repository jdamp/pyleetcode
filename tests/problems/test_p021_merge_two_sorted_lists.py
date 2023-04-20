import pytest

from data_structures import LinkedList
from problems.p021_merge_two_sorted_lists import merge_lists

examples = [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0])
]


@pytest.mark.parametrize("list1,list2,expected", examples)
def test_merge_lists(list1, list2, expected):
    linked_list1 = LinkedList(list1)
    linked_list2 = LinkedList(list2)
    assert merge_lists(linked_list1, linked_list2).to_value_list() == expected
