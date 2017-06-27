#Paul An
#is this binary tree a BST?
#This program creates an array based on an in-order traversal of the given Binary Tree.
#It compares the sum starting at 0. 0 with 1, 2 with 3, up to n-1 with n to see if the sequence is ordered correctly.

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    inorder_array = []
    inorder_array = create_array(root, inorder_array)
    return parse_array(inorder_array)

def create_array(node, inorder_array):
    if (node.left != None):
        create_array(node.left, inorder_array)
    inorder_array.append(node.data)
    if (node.right != None):
        create_array(node.right, inorder_array)
    return inorder_array

def parse_array(inorder_array):
    for i in range(len(inorder_array)-1):
        if ((inorder_array[i] - inorder_array[i+1])!= -1):
            return False
    return True

