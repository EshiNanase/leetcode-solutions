# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(str(head.val))
            head = head.next
        if ''.join(values) == ''.join(values)[::-1]:
            return True
        else:
            return False