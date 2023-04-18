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

    @classmethod
    def from_list(cls, numbers: list[int]) -> LinkedList:
        new_list = LinkedList()
        # Loop over numbers in reverse since insertion at the start of the linked list is O(1)
        for num in reversed(numbers):
            new_list.add_to_start(num)
        return new_list

    def add_to_start(self, val: int):
        """
        Inserts an element at the start of the LinkedList
        Runtime O(1)
        :param val:
        :return:
        """
        tmp_node = ListNode(val)
        tmp_node.next = self.head
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

    def pop(self):
        """
        Removes the last element from the LinkedList
        :return:
        """

    def __node__iter(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __iter__(self):
        for node in self.__node__iter():
            yield node.val

    def __str__(self):
        link_symbol = " -> "
        parts = []
        for node_val in self:
            parts.append(str(node_val))
            parts.append(link_symbol)
        # remove last link symbol
        parts.pop()
        return "".join(parts)