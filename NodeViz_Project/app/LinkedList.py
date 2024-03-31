# Definition for singly-linked list.
# project/app/views.py
from django.http import JsonResponse
from django.shortcuts import render
import os
import traceback
import sys
import io
from treevizer import to_png
import treevizer


# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy_head = Node()
        current = dummy_head

        while l1 or l2 or carry:
            x = l1.data if l1 else 0
            y = l2.data if l2 else 0

            total_sum = x + y + carry
            carry = total_sum // 10

            current.next = Node(total_sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Creating first linked list: 2 -> 4 -> 3 (representing number 342)
node3 = Node(3)
node4 = Node(4, node3)
node2 = Node(2, node4)

# Creating second linked list: 5 -> 6 -> 4 (representing number 465)
node4b = Node(4)
node6 = Node(6, node4b)
node5 = Node(5, node6)

# Creating an instance of the Solution class
sol = Solution()

# Adding the two numbers represented by the linked lists
result_head = sol.addTwoNumbers(node2, node5)

# Printing the result linked list: 7 -> 0 -> 8 (representing number 807)
print_linked_list(result_head)


to_png(
    result_head,
    structure_type="ll",
    dot_path="llworking.dot",
    png_path="llworking.png",
)
