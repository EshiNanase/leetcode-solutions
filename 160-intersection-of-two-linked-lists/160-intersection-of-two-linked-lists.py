# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1, list2 = headA, headB
        while list1 != list2:
            list1 = headB if not list1 else list1.next
            list2 = headA if not list2 else list2.next
        return list1