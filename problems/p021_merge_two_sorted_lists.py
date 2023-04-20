"""
URL: https://leetcode.com/problems/merge-two-sorted-lists/
DESCRIPTION:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
from data_structures import LinkedList, ListNode


def merge_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """
    Iterative approach
    :param list1:
    :param list2:
    :return:
    """
    this_curr = list1.head
    other_curr = list2.head
    dummy = curr = ListNode(0)
    while this_curr and other_curr:
        if this_curr.val < other_curr.val:
            curr.next = this_curr
            this_curr = this_curr.next
        else:
            curr.next = other_curr
            other_curr = other_curr.next
        curr = curr.next
    if not this_curr:
        curr.next = other_curr
    if not other_curr:
        curr.next = this_curr
    new_list = LinkedList()
    new_list.head = dummy.next
    return new_list

