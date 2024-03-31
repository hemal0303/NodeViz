from django.http import JsonResponse
from django.shortcuts import render
import os
import traceback
import sys
import io
from treevizer import recursion_viz, recursion_to_png, to_png
import ast
import treevizer


class Node:
    def __init__(self, key=0, data=0, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def has_parent(self):
        return self.parent is not None

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(f"Key: {self.key}, Data: {self.data}")
        if self.right:
            self.right.print_inorder()

    def print_preorder(self):
        print(f"Key: {self.key}, Data: {self.data}")
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(f"Key: {self.key}, Data: {self.data}")


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        # Swap left and right subtrees
        root.left, root.right = root.right, root.left

        # Update parent attribute for left and right child nodes
        if root.left:
            root.left.parent = root
        if root.right:
            root.right.parent = root

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Creating a Binary Search Tree (BST)
bst = Node(4, "Root")
bst.left = Node(2, "Left Child", parent=bst)
bst.right = Node(7, "Right Child", parent=bst)
bst.left.left = Node(1, "Left Child's Left Child", parent=bst.left)
bst.left.right = Node(3, "Left Child's Right Child", parent=bst.left)
bst.right.left = Node(6, "Right Child's Left Child", parent=bst.right)
bst.right.right = Node(9, "Right Child's Right Child", parent=bst.right)

# Creating an instance of the Solution class
sol = Solution()

print("Original BST Inorder Traversal:")
bst.print_inorder()

# Inverting the BST
# inverted_bst = sol.invertTree(bst)

# print("\nInverted BST Inorder Traversal:")
# inverted_bst.print_inorder()


to_png(
    bst,
    structure_type="bbt",
    dot_path="bst.dot",
    png_path="bst.png",
)
visualizer = TreeVisualizer()
visualizer.add_node(bst)

# Save visualization as GIF
visualizer.save_gif("tree_visualization.gif")
