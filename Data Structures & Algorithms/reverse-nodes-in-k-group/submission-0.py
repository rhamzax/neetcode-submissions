# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # make sure at least k nodes remain
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        
        index = 0
        prev, kthNode = None, head
        while index != k and kthNode:
            prev = kthNode
            kthNode = kthNode.next
            index += 1
        prev.next = None
        
        l1 = self.reverseList(head)
        l2 = self.reverseKGroup(kthNode, k)
        temp = l1
        while temp.next:
            temp = temp.next
        temp.next = l2
        return l1
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
           