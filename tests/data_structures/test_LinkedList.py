import pytest

from data_structures import ListNode, LinkedList

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.fixture
def empty_list() -> LinkedList:
    return LinkedList()


@pytest.fixture
def length1_list() -> LinkedList:
    linked_list = LinkedList()
    linked_list.add_to_start(1)
    return linked_list


@pytest.fixture
def prepared_list() -> LinkedList:
    linked_list = LinkedList()
    linked_list.add_to_start(3)
    linked_list.add_to_start(2)
    linked_list.add_to_start(1)
    return linked_list


@pytest.fixture
def list_with_duplicates() -> LinkedList:
    linked_list = LinkedList.from_value_list([1, 2, 3, 3, 2, 3, 4])
    return linked_list


@pytest.fixture
def list_with_one_value() -> LinkedList:
    linked_list = LinkedList.from_value_list([5, 5, 5, 5, 5])
    return linked_list


class TestListNode:
    def test_init(self):
        empty_node = ListNode()
        assert empty_node.val == 0
        assert not empty_node.next
        node2 = ListNode(2)
        assert node2.val == 2
        node1 = ListNode(1, next=node2)
        assert node1.val == 1
        assert node1.next == node2


class TestLinkedList:
    def test_init(self, empty_list):
        assert not empty_list.head

        setup_list = [99, -1, 5, 3]
        linked_list2 = LinkedList.from_value_list(setup_list)
        assert linked_list2.head.val == 99
        assert linked_list2.to_value_list() == setup_list

    def test_add_to_start(self):
        linked_list = LinkedList()
        linked_list.add_to_start(2)
        linked_list.add_to_start(1)
        assert linked_list.head.val == 1
        assert linked_list.head.next.val == 2
        logger.info(linked_list.to_value_list())
        assert linked_list.to_value_list() == [1, 2]
        assert(len(linked_list) == 2)

    def test_append(self, prepared_list):
        prepared_list.append(4)
        assert prepared_list.to_value_list() == [1, 2, 3, 4]
        assert(len(prepared_list) == 4)

    def test_remove(self, empty_list, prepared_list, list_with_duplicates, list_with_one_value):
        empty_list.remove(1)
        assert not empty_list.to_value_list()

        prepared_list.remove(2)
        assert prepared_list.to_value_list() == [1, 3]

        print("Duplicates: ", list_with_duplicates)
        list_with_duplicates.remove(3)
        assert list_with_duplicates.to_value_list() == [1, 2, 2, 4]

        list_with_one_value.remove(4)
        assert list_with_one_value.to_value_list() == [5, 5, 5, 5, 5]
        list_with_one_value.remove(5)
        assert not list_with_one_value.to_value_list()

    def test_str(self, empty_list, prepared_list):
        assert str(empty_list) == ""
        assert str(prepared_list) == "1 -> 2 -> 3"
