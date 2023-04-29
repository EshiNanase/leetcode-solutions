# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return head
        if not head.next:
            return head if head.val != val else None
        
        new_head = ListNode()
        new_head_node = new_head
        while head:
            if head.val != val:
                if new_head_node.val:
                    new_head_node.next = ListNode(head.val)
                    new_head_node = new_head_node.next
                else:
                    new_head_node.val = head.val
                    
            head = head.next
        if not new_head.val:
            return None
        return new_head