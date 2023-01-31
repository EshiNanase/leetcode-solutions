# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def insert(self, value):
        node = ListNode(val=value)
        if self.val is None:
            self.val = node
            return
        
        current_node = self
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next
                
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        def make_simple(list_simple, list_linked):
            list_simple.append(list_linked.val)
            if list_linked.next is not None:
                list_linked = list_linked.next
                make_simple(list_simple, list_linked)
            return list_simple[::-1]
        
        first = make_simple([], head)
        final = ListNode(val=first[0], next=None)
        
        for i in first[1:]:
            final.insert(i)
        return final
                
        