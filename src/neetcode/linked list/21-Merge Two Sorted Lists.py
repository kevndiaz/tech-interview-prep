from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        point = result

        while list1 and list2:
            if list1.val < list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list2.next

            point = point.next

        if list1:
            point.next = list1
        elif list2:
            point.next = list2

        return result.next