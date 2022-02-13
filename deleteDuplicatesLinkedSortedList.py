class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummyNode = ListNode()
    dummyNode.next = head
    checkingNode = head
    holdingNode = dummyNode
    while checkingNode != None:
        if checkingNode.next and checkingNode.val == checkingNode.next.val:
            while checkingNode.next and checkingNode.val == checkingNode.next.val:
                checkingNode = checkingNode.next
            holdingNode.next = checkingNode.next
            checkingNode = holdingNode.next
        else:
            holdingNode = holdingNode.next
            checkingNode = checkingNode.next
    return dummyNode.next
print('hi')