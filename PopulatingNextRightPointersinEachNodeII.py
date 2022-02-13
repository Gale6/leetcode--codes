
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        head = None
        prev = None
        curr = root
        while curr != None:
            while curr != None:
                if curr.left != None:
                    if head == None:
                        head = curr.left
                        prev = curr.left
                    else:
                        prev.next = curr.left
                        prev = prev.next


                if curr.right != None:
                    if head == None:
                        head = curr.right
                        prev = curr.right
                    else:
                        prev.next = curr.right
                        prev = prev.next


                curr = curr.next





            curr = head
            head = None
            prev = None

        return root