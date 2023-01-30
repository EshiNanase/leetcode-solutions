# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                
        def sum_linked(summed, l):
            if l.next is not None:
                summed.append(l.val)
                return sum_linked(summed, l.next)
            else:
                summed.append(l.val)
                return summed
        
        first_number = ''.join(str(i) for i in sum_linked([], l1)[::-1])
        second_number = ''.join(str(i) for i in sum_linked([], l2)[::-1])
        third_number = list(str(int(first_number) + int(second_number))[::-1])
        third_number = [int(i) for i in third_number]
        
        head = ListNode(third_number[0])
        current = head
        for i in range(1, len(third_number)):
            current.next = ListNode(third_number[i])
            current = current.next
                       
        return head
    