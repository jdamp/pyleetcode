"""
LeetCode class for singly-linked list
"""
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next is other.next


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.size: int = 0
        self._pos: int = 0
        self._current: Optional[ListNode] = self.head

    @classmethod
    def from_value_list(cls, numbers: list[int]) -> LinkedList:
        new_list = LinkedList()
        # Loop over numbers in reverse since insertion at the start of the linked list is O(1)
        for num in reversed(numbers):
            new_list.add_to_start(num)
        return new_list

    def to_value_list(self):
        return [node.val for node in self]

    def add_to_start(self, val: int):
        """
        Inserts an element at the start of the LinkedList
        Runtime O(1)
        :param val:
        :return:
        """
        tmp_node = ListNode(val)
        tmp_node.next = self.head
        self.size += 1
        self.head = tmp_node

    def append(self, val: int):
        """
        Inserts an element at the end of the LinkedList
        Runtime O(n)
        :param val:
        :return:
        """
        tmp_node = ListNode(val)
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = tmp_node
        self.size += 1

    def remove(self, val: int):
        """
        Removes all nodes with a value of val
        :param val:
        :return:
        """
        dummy_node = ListNode(0, next=self.head)
        curr_node = dummy_node
        while curr_node.next:
            print(self)
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        self.head = dummy_node.next
        print(self)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        return self.size

    def __str__(self):
        link_symbol = " -> "
        parts = []
        for node in self:
            parts.append(str(node.val))
            parts.append(link_symbol)
        # remove last link symbol if we have at least one node
        if parts:
            parts.pop()
        return "".join(parts)

    def __repr__(self):
        return f"<LinkedList: ({self})>"
