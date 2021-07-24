# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        last = None
        first_node = True
        while head.next is not None:
            temp = head.next
            if first_node:
                head.next = None
                first_node = False
            else:
                head.next = last
            last = head
            head = temp

        head.next = last
        return head


def print_LinkedList(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(
        val=4, next=ListNode(val=5, next=None)))))
    # head = ListNode(val=1, next=ListNode(val=2, next=None))
    # head = ListNode(val=1, next=None)
    # head = None

    print(print_LinkedList(head), "\n\n****\n")
    print(print_LinkedList(solution.reverseList(head)))
