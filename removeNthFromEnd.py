def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    f = s = head
    for _ in range(n):
        f = f.next
    if not f:
        return head.next
    while f.next:
        f = f.next
        s = s.next
    s.next = s.next.next
    return head