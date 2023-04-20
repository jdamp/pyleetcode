"""
URL: https://leetcode.com/problems/remove-linked-list-elements/
DESCRIPTION: description
"""
from data_structures import LinkedList, ListNode
from typing import Optional


def remove_elements(linked_list: Optional[LinkedList], val: int) -> Optional[LinkedList]:
    linked_list.remove(val)
    return linked_list
