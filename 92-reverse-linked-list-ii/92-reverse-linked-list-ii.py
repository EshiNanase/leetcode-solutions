# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        values = []
        
        dummy = head
        while dummy:
            values.append(dummy.val)
            dummy = dummy.next
        
        values = values[:left-1] + list(reversed(values[left-1:right])) + values[right:]
        
        head = ListNode(values.pop(0))
        dummy = head
        for value in values:
            dummy.next = ListNode(value)
            dummy = dummy.next
        
        return head
        