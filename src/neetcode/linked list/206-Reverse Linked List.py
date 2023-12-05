# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        temp = []
        while head:
            temp.append(head.val)
            head = head.next

        result = ListNode()
        current = result

        while temp:
            current.next = ListNode(temp.pop())
            current = current.next

        return result.next
