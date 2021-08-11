#  You are given two non-empty linked lists representing two non-negative integers. The digits
#  are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers
#  and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_sum = l1.val + l2.val
        sum_head = ListNode(cur_sum % 10, None)
        result_head = sum_head
        reminder = 1 if cur_sum > 9 else 0
        l1 = l1.next
        l2 = l2.next
        while l1 is not None and l2 is not None:
            cur_sum = l1.val + l2.val + reminder
            reminder = 0
            if cur_sum > 9:
                reminder = 1
            sum_head.next = ListNode(cur_sum % 10, None)
            sum_head = sum_head.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            cur_sum = l1.val + reminder
            reminder = 0
            if cur_sum > 9:
                reminder = 1
            sum_head.next = ListNode(cur_sum % 10, None)
            sum_head = sum_head.next
            l1 = l1.next

        while l2 is not None:
            cur_sum = l2.val + reminder
            reminder = 0
            if cur_sum > 9:
                reminder = 1
            sum_head.next = ListNode(cur_sum % 10, None)
            sum_head = sum_head.next
            l2 = l2.next

        if reminder == 1:
            sum_head.next = ListNode(1, None)
        return result_head


def print_LinkedList(head):
    temp = head
    while temp is not None:
        print(temp.val, '  ->  ', end='')
        temp = temp.next
    print('None')


if __name__ == '__main__':
    solution = Solution()
    # l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    # l2 = ListNode(5, ListNode(6, ListNode(4, None)))

    # l1 = ListNode(0, None)
    # l2 = ListNode(0, None)

    # l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
    # l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

    l1 = ListNode(9, ListNode(9, ListNode(9, None)))
    l2 = ListNode(9, ListNode(9, ListNode(9, None)))
    print_LinkedList(solution.addTwoNumbers(l1, l2))
