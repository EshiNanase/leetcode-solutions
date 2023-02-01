# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def insert(self, value):
        node = ListNode(val=value)
        this_node = self
        if this_node.val is None:
            this_node.val = node.val
            return
        while True:
            if this_node.next is not None:
                this_node = this_node.next
            else:
                this_node.next = node
                break
            
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def make_simple(list_simple, list_linked):
            list_simple.append(str(list_linked.val))
            if list_linked.next is not None:
                list_linked = list_linked.next
                make_simple(list_simple, list_linked)
            return list_simple
        
        list_simple = make_simple([], head)
        
        if len(list_simple) == 1:
            return head.next
        if len(list_simple) == 2 and n == 2:
            return head.next
        if len(list_simple) == 2 and n == 1:
            return ListNode(val=head.val)
        
        value = len(list_simple) - n
        
        current = head
        new_head = ListNode(val=None)
        count = 0
        while current:
            if count == value:
                current = current.next
                count += 1
            else:
                new_head.insert(current.val)
                current = current.next
                count += 1
        return new_head