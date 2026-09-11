"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #One pass to deep copy and create hashmap
        curr = head
        hmap = {None : None}
        while curr:
            newNode = Node(curr.val)
            hmap[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            newNode = hmap[curr]
            newNode.next = hmap[curr.next]
            newNode.random = hmap[curr.random]
            curr = curr.next
            
        return hmap[head]
