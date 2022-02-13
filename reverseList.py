def reverseList(head):
	if not head:
		return None
	if head.next:
		rev = reverseList(head.next)
		head.next.next = head
	head.next = None

	return head