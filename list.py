# Python program to demonstrate
# insert operation in binary search tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key
def insert(root, key):  # (r,15) = (13,15)
    if root is None:
        return Node(key)
    if root.val == key:
        #print("root", root.val)
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        print(root.val, end=" ")
        inorder(root.left)

        
# Driver code
a=Node(13)
a=insert(a, 12)
#a=insert(a,14)
# Print inorder traversal of the BST
inorder(a)
#preorder(a)
