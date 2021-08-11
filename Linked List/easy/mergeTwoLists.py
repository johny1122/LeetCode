# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing
# together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None

        if l1.val <= l2.val:
            result_head = l1
            l1 = l1.next
        else:
            result_head = l2
            l2 = l2.next

        current = result_head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        while l1 is not None:
            current.next = l1
            l1 = l1.next
            current = current.next

        while l2 is not None:
            current.next = l2
            l2 = l2.next
            current = current.next
        return result_head


def print_LinkedList(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
    l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
    # l1 = ListNode(val=1, next=None)
    # l2 = None
    # l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
    # l2 = ListNode(val=1, next=ListNode(val=3, next=None))

    print(print_LinkedList(solution.mergeTwoLists(l1, l2)))
    # print(print_LinkedList(solution.mergeTwoLists(None, None)))
    # print(print_LinkedList(solution.mergeTwoLists(l1, None)))

