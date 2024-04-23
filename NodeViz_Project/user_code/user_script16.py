
import treevizer
from treevizer import recursion_viz, to_png
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_location(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return filename
        counter += 1

def get_next_file_name(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return concated  # Return only the filename, not the full path
        counter += 1        

dot_path = get_next_file_location(dot_data_dir, "dot_file", '.dot')
png_path = get_next_file_location(png_data_dir, "png_file", '.png')

import treevizer
from treevizer import recursion_viz, to_png
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_name(directory, base_name):
    counter = 1
    while True:
        concated = base_name + str(counter)
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return filename
        counter += 1

dot_file_name = get_next_file_name(dot_data_dir, "dot_file")
png_file_name = get_next_file_name(png_data_dir, "png_file")

import treevizer
from treevizer import recursion_viz, to_png


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
node9 = Node(9)
node8 = Node(8, node9)
node7 = Node(7, node8)
node6 = Node(6, node7)


node5 = Node(5)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)



# Creating an instance of the Solution class
sol = Solution()

# Adding the two numbers represented by the linked lists
result_head = sol.addTwoNumbers(node1, node6)

# Printing the result linked list: 7 -> 0 -> 8 (representing number 807)
print_linked_list(result_head)


to_png(
    result_head,
    structure_type="ll",
    dot_path=dot_file_name,
    png_path=png_file_name,
)
file_name = get_next_file_name(png_data_dir, "png_file", '.png')
print(file_name)

