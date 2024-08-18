# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        """
        essentially saving ref to next node, so we dont lose it
        make it so that current ref to next node is pointing at prev
        move the two pointers up one
        """

        prev, curr = None, head

        # curr.next is basically the reference to next node
        while curr:
            # store next node temporarily in nxt
            # this is so that when reversing, we dont lose the pointer
            nxt = curr.next
            # reverses the curr node pointer, now points to prev
            # reverses the direction of the link
            curr.next = prev
            prev = curr
            curr = nxt
        # returns the head
        return prev
