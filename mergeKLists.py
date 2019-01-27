def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    lists = [n for n in lists if n]
    full = ListNode(-1)
    temp = full
    while lists:
        k = 0      
        for i in range(len(lists)):
            if lists[i].val < lists[k].val:
                k = i
        temp.next = lists[k]
        temp = temp.next
        lists[k] = lists[k].next
        if lists[k] == None:
            lists.pop(k)
    return full.next