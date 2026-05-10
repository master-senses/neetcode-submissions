# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        new_list = ListNode()
        curr = new_list

        if not list1:
            return list2
        
        if not list2:
            return list1

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
            curr.next = None
        
        if head1:
            curr.next = head1
        elif head2:
            curr.next = head2
        
        return new_list.next

