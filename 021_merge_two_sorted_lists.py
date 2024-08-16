# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # use dummy node, to not worry about edge case of inserting into empty list
        dummy = ListNode()
        tail = dummy

        # while list1 and list2 are not null, so they can be compared
        while list1 and list2:
            # if value of list1 is less than list2, insert it into tail
            if list1.val < list2.val:
                tail.next = list1
                # update list1 pointer
                list1 = list1.next
            else:
                # insert list2 value as tail and update pointer
                tail.next = list2
                list2 = list2.next
            # tail node updated regardless, hence outside
            tail = tail.next

        # what if one is empty and the other isn't
        # find the non empty list and add the rest to tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
