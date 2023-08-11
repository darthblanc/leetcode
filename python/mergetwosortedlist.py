# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rv = ListNode()
        while list2 is not None:
            rv = ListNode(list2.val, rv)
            list2 = list2.next

        print(rv)
        return list1


Solution.mergeTwoLists(ListNode(1, ListNode(2, None)), ListNode(2, ListNode(3, None)))
