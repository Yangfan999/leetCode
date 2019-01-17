    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        r = head
        while l1 and l2:
            if l1.val > l2.val:
                temp = l2
                l2 = l2.next
                head.next = temp
                head = head.next
            else:
                temp = l1
                l1 = l1.next
                head.next = temp
                head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return r.next