# https://leetcode.com/problems/add-two-numbers/

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
        sum_list = ListNode()
        sum_list_pointer = sum_list
        remainder = 0
        last_node_pointer = 0
        l1_pointer = l1
        l2_pointer = l2
        while l1_pointer is not None:
            if l1_pointer.next is not None:
                sum_list_pointer.next = ListNode()
            else:
                last_node_pointer = sum_list_pointer
                break

            if l2_pointer is not None:
                if remainder != 0:
                    curr_sum = l1_pointer.val + l2_pointer.val + remainder
                    remainder = 0
                else:
                    curr_sum = l1_pointer.val + l2_pointer.val
                if curr_sum > 9:
                    remainder = int(curr_sum / 10)
                    sum_list_pointer.val = int(curr_sum % 10)
                else:
                    sum_list_pointer.val = curr_sum
                l2_pointer = l2_pointer.next
            else:
                sum_list_pointer.val = l1_pointer.val
            l1_pointer = l1_pointer.next
            sum_list_pointer = sum_list_pointer.next

        while l2_pointer is not None:
            if l2_pointer.next is not None:
                sum_list_pointer.next = ListNode()
            else:
                last_node_pointer = sum_list_pointer
                break

            if remainder != 0:
                curr_sum = l2_pointer.val + remainder
                remainder = 0
            else:
                curr_sum = l2_pointer.val
            if curr_sum > 9:
                remainder = int(curr_sum / 10)
                sum_list_pointer.val = int(curr_sum % 10)
            else:
                sum_list_pointer.val = curr_sum
            l2_pointer = l2_pointer.next
            sum_list_pointer = sum_list_pointer.next

        if remainder != 0:
            print(remainder)
            # last_node_pointer.next = ListNode()
            # last_node_pointer.next.val = remainder
            last_node_pointer.val = remainder

        return sum_list


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode()
    l1.next = ListNode()
    l1.next.next = ListNode()
    l1.val = 2
    l1.next.val = 4
    l1.next.next.val = 3

    l2 = ListNode()
    l2.next = ListNode()
    l2.next.next = ListNode()
    l2.val = 5
    l2.next.val = 6
    l2.next.next.val = 4
    sum = s.addTwoNumbers(l1, l2)
    print(sum.val, sum.next.val, sum.next.next.val)
    # print(sum.val, sum.next.val)
