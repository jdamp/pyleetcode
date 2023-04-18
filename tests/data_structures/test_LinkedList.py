import pytest

from data_structures import ListNode, LinkedList

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@pytest.fixture
def prepared_list():
    linked_list = LinkedList()
    linked_list.add_to_start(3)
    linked_list.add_to_start(2)
    linked_list.add_to_start(1)
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
    def test_init(self):
        linked_list = LinkedList()
        assert not linked_list.head

        setup_list = [99, -1, 5, 3]
        linked_list2 = LinkedList.from_list(setup_list)
        assert linked_list2.head.val == 99
        assert list(linked_list2) == setup_list

    def test_add_to_start(self):
        linked_list = LinkedList()
        linked_list.add_to_start(2)
        linked_list.add_to_start(1)
        assert linked_list.head.val == 1
        assert linked_list.head.next.val == 2
        logger.info(list(linked_list))
        assert list(linked_list) == [1, 2]

    def test_append(self, prepared_list):
        prepared_list.append(4)
        assert list(prepared_list) == [1, 2, 3, 4]

    def test_pop(self, prepared_list):
        prepared_list.pop()
        assert list(prepared_list) == [1, 2]

    def test_str(self, prepared_list):
        assert str(prepared_list) == "1 -> 2 -> 3"


