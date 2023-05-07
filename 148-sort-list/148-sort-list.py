# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        values = []
        while head:
            
            values.append(head.val)
            head = head.next
        
        values.sort()
        
        head = ListNode(val=values[0])
        node = head
        for value in values[1:]:
            node.next = ListNode(val=value)
            node = node.next
        
        return head