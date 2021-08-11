#  Given the heads of two singly linked-lists headA and headB, return the node at which the two
#  lists intersect. If the two linked lists have no intersection at all, return null

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.next = next
        self.val = x


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length_A = 0
        temp = headA
        while temp:
            length_A += 1
            temp = temp.next

        length_B = 0
        temp = headB
        while temp:
            length_B += 1
            temp = temp.next

        if length_A > length_B:
            steps_to_match = length_A - length_B
            while steps_to_match > 0:
                headA = headA.next
                steps_to_match -= 1

        else:
            steps_to_match = length_B - length_A
            while steps_to_match > 0:
                headB = headB.next
                steps_to_match -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


if __name__ == '__main__':
    solution = Solution()

    intersection = ListNode(8, ListNode(4, ListNode(5)))
    head1 = ListNode(4, ListNode(1, intersection))
    head2 = ListNode(5, ListNode(6, ListNode(1, intersection)))

    # head1 = ListNode(4, ListNode(1, None))
    # head2 = ListNode(5, ListNode(6, ListNode(1, None)))

    print(intersection)
    print(solution.getIntersectionNode(head1, head2))
