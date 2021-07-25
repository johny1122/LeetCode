# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer. Internally, pos is used to denote the
# index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None or head.next is None:
            return False

        pointer_1 = pointer_2 = head

        while pointer_1 and pointer_2 and pointer_2.next:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
            if pointer_1 == pointer_2:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    last = ListNode(-4)
    third = ListNode(0)
    third.next = last
    second = ListNode(2)
    second.next = third
    head = ListNode(3)
    head.next = second
    last.next = second  # if None, has not cycle
    # -----------------------
    # last = ListNode(2)
    # head = ListNode(1)
    # head.next = last
    # last.next = head  # if None, has not cycle
    # -----------------------
    # head = ListNode(1)
    # -----------------------
    # head = None

    print(solution.hasCycle(head))
