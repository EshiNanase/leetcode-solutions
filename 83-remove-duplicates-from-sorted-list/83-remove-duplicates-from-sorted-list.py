# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        
        while head:
            if head.val not in values:
                values.append(head.val)
            head = head.next
        
        if not values:
            return None
            
        head = ListNode(values[0])
        node = head
        for i in values[1:]:
            node.next = ListNode(i)
            node = node.next
        return head
            