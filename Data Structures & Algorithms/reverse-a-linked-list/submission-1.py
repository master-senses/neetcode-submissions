# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        #  empty = ListNode(None, head)

        curr = head
        prev = None
        next_n = None
        while curr.next:
            next_node = curr.next
            if next_node:
                print(next_node.val)
            curr.next = prev
            print(curr.val)
            prev = curr
            curr = next_node
        curr.next = prev
        # print(head.next)
        return curr


