# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length - n == 0:
            return head.next
        index = 0
        prev, curr = None, head
        while curr:
            
            if index == length-n:
                print(index)
                curr = curr.next
                prev.next = curr
                break
            prev = curr
            curr = curr.next
            index += 1
        return head